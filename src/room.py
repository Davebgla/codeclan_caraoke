

class Room:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
        self.guests = []
        self.songs = []
    

    def guest_count(self):
        return len(self.guests)

    def add_guest(self, add_to_room):
        self.guests.append(add_to_room)

    def remove_guest(self, remove_from_room):
        self.guests.remove(remove_from_room)

    def song_count(self):
        return len(self.songs)

    def add_song(self, add_song_to_room):
        self.songs.append(add_song_to_room)














    # def check_in(self, guest1):
    #     self.guests_in_room.append(guest1)

    # def check_out(self, guest2):
    #     self.guests_in_room.remove(guest2)

    # def add_song(self, song):
    #     self.song_choice.append(song)














    








   