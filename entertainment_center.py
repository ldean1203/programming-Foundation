import fresh_tomatoes
import media

'''use Movie class to create some instance with
    different movie title,detail,image and trailer url'''
despicable_me3 = media.Movie('Despicable Me 3',
                             'What does it take to be a successful '
                             'supervillain? An arsenal of deadly weapons, '
                             'a mad scientist at your disposal, an army of '
                             'adorable minions (who have adventures of their '
                             'own)... and three lovable girls to keep you '
                             'grounded. Conquering the world has never been '
                             'so fun and funny.',
                             'https://resizing.flixster.com/bPDwOYjegtZKPlStwL'
                             'E-yDv2tSI=/206x305/v1.bTsxMjMzNTI3NztqOzE3Mzc3Oz'
                             'EyMDA7MzE1ODs1MDAw',
                             'https://www.youtube.com/watch?'
                             'v=euz-KBBfAAo')

wonder_woman = media.Movie('Wonder Woman',
                           'The DC Universe hits the big screen, '
                           'bringing back Superman and Batman; and '
                           'introducing for the first time in the '
                           'movies classic comic book characters '
                           'like Wonder Woman, Aquaman, and more.',
                           'https://resizing.flixster.com/td_SGsFL'
                           '9oomA4zxD0G2QfzlSJ0=/206x305/v1.bTsxMj'
                           'QxMTMzMTtqOzE3Mzc4OzEyMDA7NDA1MDs2MDAw',
                           'https://www.youtube.com/watch?'
                           'v=VSB4wGIdDwo')

GUARDIANS_OF_THE_GALAXY2 = media.Movie('GUARDIANS OF THE GALAXY VOL. 2',
                                       'From Iron Man to Captain America to '
                                       'Daredevil, Guardians of the Galaxy, '
                                       'Jessica Jones, and more, the MCU '
                                       'brings some of the most legendary '
                                       'comic heroes -- and some lesser '
                                       'known ones -- to vibrant, colorful,'
                                       ' action-packed life.',
                                       'https://resizing.flixster.com/'
                                       '-Ogfn9eMJWdDjFUMPsxGKjuDggc=/'
                                       '206x305/v1.bTsxMjMyMzE1NjtwOz'
                                       'E3Mzc3OzEyMDA7NTkxOzg3Ng',
                                       'https://www.youtube.com/watch?'
                                       'v=duGqrYw4usE')

DOCTOR_STRANGE = media.Movie('DOCTOR STRANGE',
                             'Doctor Strange artfully balances its outré '
                             'source material against the blockbuster '
                             'constraints of the MCU, delivering a '
                             'thoroughly entertaining superhero origin '
                             'story in the bargain.',
                             'https://resizing.flixster.com/w1S1AVe_'
                             'YtP9-Yrh2uSwavnqKxU=/206x305/v1.bTsxMj'
                             'E3OTkzMTtqOzE3Mzc1OzEyMDA7Mzg3OzU3Ng',
                             'https://www.youtube.com/watch?v=HSzx-zryEgM')

Captain_America_Civil_War = media.Movie('Captain America: Civil War',
                                        'Captain America: Civil War begins the'
                                        ' next wave of Marvel movies with an '
                                        'action-packed superhero blockbuster '
                                        'boasting a decidedly non-cartoonish '
                                        'plot and the courage to explore '
                                        'thought-provoking themes.',
                                        'https://resizing.flixster.com/Nt0BJ9'
                                        '_u1R1HzwLsB9Lse7Wt8Xo=/180x240/v1.'
                                        'bTsxMTY5MDA3MDtwOzE3MzcwOzEyMDA7N'
                                        'Dg4OzcyMA',
                                        'https://www.youtube.com/watch?'
                                        'v=dKrVegVI0Us')

Black_Panther = media.Movie('Black Panther',
                            'Black Panther follows TChalla who, after the '
                            'events of "Captain America: Civil War,returns '
                            'home to the isolated, technologically advanced '
                            'African nation of Wakanda to take his place as '
                            'King. However, when an old enemy reappears on '
                            'the radar, TChallas mettle as King and Black '
                            'Panther is tested when he is drawn into a '
                            'conflict that puts the entire fate of Wakanda '
                            'and the world at risk.',
                            'https://resizing.flixster.com/Lnimh1aa0rRZ'
                            'jwGNJlW7mWyv1XQ=/206x305/v1.bTsxMjQyMjAzO'
                            'DtqOzE3Mzc4OzEyMDA7MTY4ODsyNTAw',
                            'https://www.youtube.com/watch?v=dxWvtMOGAhw')
'''the open_movies_page only accept a list ,
    so put all the Movie instances into a list'''
movie_list = [despicable_me3, wonder_woman, GUARDIANS_OF_THE_GALAXY2,
              DOCTOR_STRANGE, Captain_America_Civil_War, Black_Panther]
'''call the open_movies_page ,create the html page'''
fresh_tomatoes.open_movies_page(movie_list)
