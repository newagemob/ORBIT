'''
Use GPT-3.5-Turbo to summarize news articles from OpenBB Terminal's news outlet - each stock should have a paragraph summary unless there is major news, then it should have a full article summary.
'''

import openai
from openbb_terminal.sdk import openbb
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Get OpenAI API key
openai.api_key = ""

# Set up OpenBB SDK with PyPi
# openbb.api_key = ""
# openbb.api_secret = ""

# Get all articles from OpenBB Terminal's news outlet


def get_general_news() -> list:
    """
    Gets all articles from OpenBB Terminal's news outlet.

    Returns:
    list: A list of articles.
    """

    articles = []
    for article in openbb.news():
        print(article)
        # articles.append(article["title"])

    # Set up Selenium Firefox driver to save articles' text and titles
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    for article in articles:
        driver.get(article)
        title = driver.find_element_by_tag_name("h1").text
        text = driver.find_element_by_class_name("article-text").text

        # Feed article text to OpenAI's API for summarization
        prompt = "Please summarize the following article:\n\n" + text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        summary = response.choices[0].text
        print(f"Title: {title}")
        print(f"Summary: {summary}\n")

    # Quit Selenium Firefox driver
    driver.quit()

    return articles


def get_stock_news(ticker):
    """
    Gets specific stock ticker's news articles from OpenBB Terminal's news outlet.
    
    Returns:
    list: A list of articles.
    """

    articles = []
    for article in openbb.get_news(ticker):
        articles.append(article["title"])

    # Set up Selenium Firefox driver to save articles' text and titles
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    for article in articles:
        driver.get(article)
        title = driver.find_element_by_tag_name("h1").text
        text = driver.find_element_by_class_name("article-text").text

        # Feed article text to OpenAI's API for summarization
        prompt = "Please summarize the following article:\n\n" + text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        summary = response.choices[0].text
        print(f"Title: {title}")
        print(f"Summary: {summary}\n")

    # Quit Selenium Firefox driver
    driver.quit()
