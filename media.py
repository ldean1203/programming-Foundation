import webbrowser


class Movie():
    '''The Movie class create a instance of movie,need the title of movie,
    the storyline,the poster image url and trailer url'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
