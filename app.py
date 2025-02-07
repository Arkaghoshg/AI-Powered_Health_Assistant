import streamlit as st                         #to create the web app
import nltk                                    #for working with the text data
from transformers import pipeline              #using exteernal pretrained model 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbo = pipeline("text -generation",model = "distilgpt2")

def main():
     st.title("Health Assistant Chatbot")
     
main()