# BeautifulSoup 4 documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Information about selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

# Data Pretty Printer: https://docs.python.org/3/library/pprint.html

# Link to Scrapy documentation: https://docs.scrapy.org/en/latest/

import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Function to fetch and parse HTML content from a given URL
def fetch_page_content(url):
    """
    Fetches the HTML content of a given URL and parses it using BeautifulSoup.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None

# Function to extract story links and subtext from a parsed HTML page
def extract_links_and_subtext(soup):
    """
    Extracts story links and their associated metadata (subtext) from a BeautifulSoup object.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the page.

    Returns:
        tuple: A tuple containing two lists - story links and subtext metadata.
    """
    if soup:
        links = soup.select('.storylink')  # Select all story links
        subtext = soup.select('.subtext')  # Select associated metadata (e.g., votes)
        return links, subtext
    return [], []

# Function to sort stories by votes in descending order
def sort_stories_by_votes(stories):
    """
    Sorts a list of stories by their vote count in descending order.

    Args:
        stories (list): List of dictionaries containing story details.

    Returns:
        list: Sorted list of stories by votes in descending order.
    """
    return sorted(stories, key=lambda story: story['votes'], reverse=True)

# Function to filter and structure stories with more than 99 votes
def create_custom_hn(links, subtext):
    """
    Filters stories with more than 99 votes and structures them into a list of dictionaries.

    Args:
        links (list): List of BeautifulSoup elements representing story links.
        subtext (list): List of BeautifulSoup elements representing metadata for each story.

    Returns:
        list: A sorted list of dictionaries containing title, link, and vote count for each story.
    """
    hn_stories = []
    
    for idx, item in enumerate(links):
        title = item.getText()  # Extract the title of the story
        href = item.get('href', None)  # Extract the URL of the story
        vote_elements = subtext[idx].select('.score')  # Extract vote count
        
        if vote_elements:  # Check if votes are present
            points = int(vote_elements[0].getText().replace(' points', ''))
            if points > 99:  # Filter stories with more than 99 votes
                hn_stories.append({'title': title, 'link': href, 'votes': points})
    
    return sort_stories_by_votes(hn_stories)

# Main script execution
if __name__ == "__main__":
    # URLs for Hacker News pages
    url_page_1 = 'https://news.ycombinator.com/news'
    url_page_2 = 'https://news.ycombinator.com/news?p=2'

    # Fetch and parse content from both pages
    soup_page_1 = fetch_page_content(url_page_1)
    soup_page_2 = fetch_page_content(url_page_2)

    # Extract links and subtext from both pages
    links_page_1, subtext_page_1 = extract_links_and_subtext(soup_page_1)
    links_page_2, subtext_page_2 = extract_links_and_subtext(soup_page_2)

    # Combine links and subtext from both pages for processing
    all_links = links_page_1 + links_page_2
    all_subtext = subtext_page_1 + subtext_page_2

    # Create a custom Hacker News feed with filtered and sorted stories
    top_stories = create_custom_hn(all_links, all_subtext)

    # Pretty-print the top stories
    pprint(top_stories)