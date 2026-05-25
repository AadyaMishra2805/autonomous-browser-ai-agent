import streamlit as st
import requests

# PAGE CONFIG
st.set_page_config(
    page_title="Autonomous Browser AI Agent",
    page_icon="🤖",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0B0F19;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #0B0F19;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-top: 5px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #9CA3AF;
    font-size: 16px;
    margin-bottom: 20px;
}

.stTextInput > div > div > input {
    background-color: #1A1F2E;
    color: white;
    border-radius: 15px;
    border: 1px solid #333;
    padding: 10px;
    font-size: 16px;
}

.stButton > button {
    background: linear-gradient(90deg, #2563EB, #4F46E5);
    color: white;
    border-radius: 14px;
    border: none;
    padding: 10px 22px;
    font-size: 16px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    """
    <div class="title">
        🤖 Autonomous Browser AI Agent
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Search the web intelligently using AI-powered browser automation
    </div>
    """,
    unsafe_allow_html=True
)

# INPUT
query = st.text_input(
    "",
    placeholder="Search laptops, phones, AI tools..."
)

# BUTTON
search = st.button("🚀 Search")

# SEARCH
if search and query:

    with st.spinner("Searching the web..."):

        try:

            # YOUR N8N PRODUCTION WEBHOOK
            url ="https://aadya.app.n8n.cloud/webhook-test/search-agent"

            response = requests.get(
                url,
                params={"query": query}
            )

            data = response.json()

            st.markdown("## 🔍 Results")

            if "results" in data and len(data["results"]) > 0:

                for result in data["results"]:

                    st.subheader(result["title"])

                    st.link_button(
                        "🔗 Visit Website",
                        result["link"]
                    )

                    st.divider()

            else:

                st.error("No results found")

        except Exception as e:

            st.error(f"Error: {e}")