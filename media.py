#Movie class definition

class Movie():
    '''Class definition for a movie'''
    def __init__(self, title, synopsis, poster, trailer_url):
        self.title = title
        self.synopsis=synopsis
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_url
