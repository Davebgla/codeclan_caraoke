from src.guest import Guest
from src.song import Song

class Room:
    def __init__(self, name):
        self.name = name
        self.guests = [Guest, Guest]
        self.songs = [Song, Song]

    def guest_count(self):
        return len(self.guests)

    def song_count(self):
        return len(self.songs)


    def check_in_guest(self, guest):
        self.guests.append(guest)

    
    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
    

    def room_is_full(self, level):
        if self.guest_count > level:
            return "Too full!"











   