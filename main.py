import streamlit as st
import pickle
with open('news.pkl','rb') as file:
    model=pickle.load(file)
with open ('cv.pkl','rb') as file:
    count_vectorizer=pickle.load(file)    
user_input=st.text_area("TELL ME FRESH NEWS")
if st.button("classifier"):
    preprocess=count_vectorizer.transform([user_input])
    result = model.predict(preprocess)[0]
    if(result==1):
        st.success("Prediction: This is Real News!")
    else:
            st.error("Prediction: This is Fake News!")