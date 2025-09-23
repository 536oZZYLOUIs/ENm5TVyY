# 代码生成时间: 2025-09-24 01:28:41
import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

"""
Web Scraper Streamlit App

This application allows users to input a URL and retrieve the HTML content from the webpage.
"""

# Streamlit title
st.title('Web Content Scraper')

# Text input for URL
url_input = st.text_input('Enter a URL:', '')

# Function to fetch and display HTML content
def fetch_html_content(url):
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Return the HTML content
        return soup.prettify()
    except requests.exceptions.HTTPError as errh:
        st.error(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        st.error(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        st.error(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        st.error(f'Oops: Something Else: {err}')
    except Exception as e:
        st.error(f'An unexpected error occurred: {e}')

# Button to trigger HTML content fetching
if st.button('Scrape HTML'):
    if url_input:
        # Fetch and display HTML content
        html_content = fetch_html_content(url_input)
        st.code(html_content, language='html')
    else:
        st.warning('Please enter a URL to scrape.')
