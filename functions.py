from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def generate_url(query):
    return "https://www.dictionary.com/browse/" + "%20".join(query.split())

def antonym(query):
    url = "https://www.antonym.com/synonyms/"+ "%20".join(query.split())
    request = requests.get(url).text
    soup = BeautifulSoup(request, "html.parser")
    antonym_tags = soup.find_all('div', "card full-width mdc-card type-antonym")
    return antonym_tags[0].contents[3].contents[1].contents[0].strip()
    
def extract(url):
    request = requests.get(url).text
    soup = BeautifulSoup(request, "html.parser")
    block = soup.find_all('div', 'css-1avshm7 e16867sm0')
    header = block[0].contents[0]
    pos = block[0].contents[1].contents[0]
    definition = block[0].contents[1].contents[1]
    return (header, pos, definition)

def page(query):
    query_ant = antonym(query)
    header, pos = extract(generate_url(query))[:2]
    definition = extract(generate_url(query_ant))[2]
    return (header, pos, definition)