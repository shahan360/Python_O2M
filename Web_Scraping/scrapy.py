
"""
Description:
This script scrapes the top news stories from Hacker News (https://news.ycombinator.com/)
and filters the stories based on a minimum vote threshold. It uses the `requests` library 
to fetch the webpage and `BeautifulSoup` for parsing and extracting relevant data.

Enhancements:
- Improved readability with detailed comments and structured code.
- Added error handling for HTTP requests.
- Modularized the code with functions for better reusability.
- Enhanced sorting logic for clarity.
"""

import requests
from bs4 import BeautifulSoup
import pprint  # Pretty print for better readability of output

# Constants
URL = 'https://news.ycombinator.com/'
MINIMUM_SCORE = 100  # Minimum votes required to include a story


def fetch_page_content(url):
    """
    Fetches the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the page if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page content: {e}")
        return None


def parse_news(html_content):
    """
    Parses the HTML content to extract news stories and their metadata.

    Args:
        html_content (str): The HTML content of the Hacker News page.

    Returns:
        list: A list of tuples containing news title, link, and score.
              Each tuple is in the format (title, link, score).
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract news links and metadata
    links = soup.select(".storylink")  # News story links
    subtexts = soup.select(".subtext")  # Metadata (e.g., votes)

    news_list = []

    for i in range(len(links)):
        news_title = links[i].getText()  # Extract the title text
        news_link = links[i].get("href", None)  # Extract the hyperlink (defaults to None if missing)
        votes = subtexts[i].select(".score")  # Extract votes (if available)

        # Parse vote count; default to 0 if no votes are found
        score = int(votes[0].getText().split(' ')[0]) if votes else 0

        # Include only stories with votes above the threshold
        if score > MINIMUM_SCORE:
            news_list.append((news_title, news_link, score))

    return news_list


def sort_news_by_votes(news_list):
    """
    Sorts a list of news stories by their vote count in descending order.

    Args:
        news_list (list): A list of tuples containing news title, link, and score.

    Returns:
        list: The sorted list of news stories.
    """
    return sorted(news_list, key=lambda x: x[2], reverse=True)


def main():
    """
    Main function to scrape Hacker News and display top stories based on votes.
    """
    print("Fetching Hacker News top stories...")
    
    html_content = fetch_page_content(URL)
    
    if not html_content:
        print("Failed to retrieve Hacker News content.")
        return

    # Parse and filter news stories
    news_list = parse_news(html_content)

    # Sort stories by vote count
    sorted_news = sort_news_by_votes(news_list)

    # Display results
    print("\nTop Hacker News Stories (Votes > 100):")
    pprint.pprint(sorted_news)


if __name__ == "__main__":
    main()