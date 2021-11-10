import requests,json


__all__ = ('UrbanDictionary')

class UrbanDictionary():

    def search(word):
        global content_loaded
        r = requests.get(f'https://api.urbandictionary.com/v0/define?term={word}')
        content_loaded = json.loads(r.content)

    def author():
        author = content_loaded['list'][0]['author']
        return author
    
    def definition():
        definition = content_loaded['list'][0]['definition']
        return definition
    
    def example():
        example = content_loaded['list'][0]['example']
        return example
    
    def word():
        ubword = content_loaded['list'][0]['word']
        return ubword
    
    def written_on():
        written_on = content_loaded['list'][0]['written_on'][:10]
        return written_on
    
