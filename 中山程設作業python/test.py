from datetime import datetime
import datetime
class Movie:
    local_time=datetime.datetime.now()
    def __init__(self):
        self.movie_table={
            "Iron man":"2022-05-30 08:00:00", 
            "Memory":"2022-05-30 13:00:00" , 
            "Life For Sale":"2022-05-30 15:00:00" }
    
    def add_movie(self, movie_name, movie_time):
        self.movie_table["movie_name"]=movie_time

    def find_play_time(self, name):
        print(f'The show time of the movie, {name}, is {self.movie_table[name]}')
        self.point_show_time=datetime.strptime(self.movie_table[name], "%Y-%m-%d %H%M%S")
        if self.local_time<=self.point_show_time:
            print(f'{self.local_time-self.point_show_time} before the movie.')
        else:
            print("Movie has played!")

    def __str__(self):
        return f'There are currently {len(self.movie_table)} movies on the movie playlist.'

movie=Movie()
movie.add_movie('Always', '2022-06-05 13:00:00')
#movie.add_movie(input("Please enter the movie name: "), input("Please enter the show time of the movie (year-month-day hour:minute:second):"))
movie.find_play_time(input("Please enter the movie name you want to know the playing time of:  "))
print(movie)

