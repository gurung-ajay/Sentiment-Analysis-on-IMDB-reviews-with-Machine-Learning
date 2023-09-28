import pickle
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# preprocessing input text the same way as when model was trained
lemmatizer = WordNetLemmatizer()
def clean_data(x):
  # lowercasing
  x = x.lower()
  # tokenization
  words = nltk.word_tokenize(x)
  # stop words removal
  stop_words = list(nltk.corpus.stopwords.words('english'))
  clean_words = [item for item in words if item not in stop_words]
  # lemmatization
  lemmatized_words = [lemmatizer.lemmatize(w) for w in clean_words]
  return ' '.join(lemmatized_words)


# loading Logistic Regression model
with open('LogisticRegressionIMDBClassifier.pickle', 'rb') as file:
    model = pickle.load(file)

# UI
st.title("Sentiment Analysis on IMDB movie review")

review = st.text_input("Enter movie review: ")

## when button is clicked, input text is cleaned and sent to a pipelie model 
## where it will be vectorized and predicted with Logistic Regression
if st.button("Analyze sentiment"):
    review = clean_data(review)
    prediction = model.predict([review])[0]   
    st.write(prediction)