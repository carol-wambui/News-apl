class Sources:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    def __init__(self,id,author,description,url, title,content ,publishedAt,urlToImage):
        self.id =id
        self.author = author
        self.description = description
        self.url = url
        self.title= title
        self.content = content 
        self.publishedAt= publishedAt
        self.urlToImage= urlToImage

