from src.guest import Guest
# from src.song import Song

class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = []
        self.song_choice = []
        self.fee = fee


    def check_in(self, guest1):
        self.guests_in_room.append(guest1)


    def check_out(self, guest2):
        self.guests_in_room.remove(guest2)

    def add_song(self, song2):
        self.song_choice.append(song2)














    








   