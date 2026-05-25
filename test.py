import streamlit as st
import requests

st.title("Browser Agent")

query = st.text_input("Search")

if st.button("Search"):

    url = "https://aadya.app.n8n.cloud/webhook-test/search-agent"

    response = requests.get(
        url,
        params={"query": query}
    )

    data = response.json()

    st.write(data)