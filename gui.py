import PySimpleGUI as sg
import os
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
import numpy as np
from PIL import Image
import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import sys

currdir = os.path.dirname(__file__)
if __name__ == '__main__':

  form = sg.FlexForm('GUI for the Project')  # begin with a blank form

  layout = [
          [sg.Text('Type in the topic of wikipedia, you want to get WordCloud for')],
          [sg.Text('Enter Topic', size=(15, 1)), sg.InputText('')],
          [sg.Submit(), sg.Cancel()]
         ]

  button, values = form.Layout(layout).Read() 


  title = wikipedia.search(str(values))[0]
  page =  wikipedia.page(title)

  text = page.content
  mask = np.array(Image.open(os.path.join(currdir,"cloud.png")))
  stop = set(STOPWORDS)
  wc = WordCloud(background_color="white",mask=mask,max_words=200,stopwords=stop)
  messages = nltk.sent_tokenize(text)
  corpus=[]
  lemmatizer = WordNetLemmatizer()
  stemmer = PorterStemmer()
  for i in range(len(messages)):
      temporary = re.sub('[^a-zA-Z]',' ',messages[i])
      temporary = temporary.lower()
      temporary = temporary.split()
      temporary = [stemmer.stem(word) for word in temporary if word not in set(stopwords.words('english'))]
      temporary = ' '.join(temporary)
      corpus.append(temporary)

  listToStr = ' '.join([str(elem) for elem in corpus]) 
  wc.generate(listToStr)
  wc.to_file(os.path.join(currdir,"wc.png"))

  os.system('wc.png')



