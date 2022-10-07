# py -m streamlit run main.py

import streamlit as st
import newspaper

st.title("Article scraper")

url = st.text_input("", placeholder="Paste URL and Enter")

if url:
    article = newspaper.Article(url)
    article.download()
    
    article.parse()
    authors = article.authors
    st.text(", ".join(authors))
    
    article.nlp()
    
    st.subheader("Keywords")
    key = article.keywords
    st.write(", ".join(key))
      
    tab1, tab2 = st.tabs(["Full text", "Summary"])
    with tab1:
        article.text
    with tab2:
        st.write(article.summary)