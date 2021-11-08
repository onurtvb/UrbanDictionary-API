import requests,json


__all__ = ('UrbanDictionary')

def UrbanDictionary(word):
    r = requests.get(f'https://api.urbandictionary.com/v0/define?term={word}')
    content_loaded = json.loads(r.content)
    author = content_loaded['list'][0]['author']
    definition = content_loaded['list'][0]['definition']
    example = content_loaded['list'][0]['example']
    ubword = content_loaded['list'][0]['word']
    writte_on = content_loaded['list'][0]['written_on'][:10]
    form = f'Word: {ubword}\nAuthor: {author}\nDefinition: {definition}\nExample: {example}\nWritten on: {writte_on}'
    print(form)
    
