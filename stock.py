import streamlit as st
import requests
import urllib.parse
import json


# Define the function to fetch news based on the stock name and selected keywords
def fetch_news_about(stock_name, keywords):
    client_id = "5nJ0_zmxz_XTpOqewWNY"  # Replace with your actual Naver API Client ID
    client_secret = "bB13L6YuPc"  # Replace with your actual Naver API Client Secret
    news_items = []

    for keyword in keywords:
        query = f"{stock_name} {keyword}"
        enc_text = urllib.parse.quote(query)
        url = f"https://openapi.naver.com/v1/search/news.json?query={enc_text}&display=3"

        headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            news_items.extend(response_data['items'])
        else:
            st.error(f"Error retrieving news for query '{query}': HTTP {response.status_code}")

    return news_items


# Streamlit UI components
st.set_page_config(page_title="Stock News Finder", layout="wide")
st.title("Stock News Finder")

stock_name = st.text_input("Enter the stock name to fetch news for:", "")

# List of predefined keywords
keywords = [
    "국책과제선정", "전년비 증가", "차세대 개발착수", "컨센서스 상회", "수요폭증", "호실적 기대감",
    "경영권인수", "무상증자 결정", "아이폰 수혜", "관세폭탄", "테슬라", "애플", "앤비디아",
    "마이크로소프트", "메타", "세계최초", "국내최초", "EUV", "공급임박", "HBM", "FDA승인", "출시임박", "최대실적"
]

# Allow users to select keywords they are interested in
selected_keywords = st.multiselect("Select keywords:", keywords, default=["테슬라", "애플"])

if st.button("Fetch News"):
    if stock_name and selected_keywords:
        news_items = fetch_news_about(stock_name, selected_keywords)
        if news_items:
            for idx, item in enumerate(news_items):
                st.subheader(f"News {idx + 1}: {item['title']}")
                st.write(f"Summary: {item['description']}")
                st.markdown(f"[Read more]({item['link']})")
        else:
            st.write("No news found for the selected keywords and stock name.")
    else:
        st.warning("Please enter a stock name and select at least one keyword.")

# Ensure to replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with actual values
