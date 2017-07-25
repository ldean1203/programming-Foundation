import webbrowser


class Movie():
    '''The Movie class create a instance of movie,need the title of movie,
    the storyline,the poster image url and trailer url'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_url):
        '''initialize a Movie instance with given parameters
        :param movie_title: the title of movie,will display below the poster of the movie
        :param movie_storyline: the detail of the movie
        :param poster_image: the poster of the movie, need the url of the poster image
        :param trailer_url: the trailer of the movie, also should input a url
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        '''
        when you click the movie poster, it'll show a mini window with trailer player
        '''
        webbrowser.open(self.trailer_youtube_url)
