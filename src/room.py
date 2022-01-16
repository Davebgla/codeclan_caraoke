

class Room:
    def __init__(self, name, fee, capacity):
        self.name = name
        self.fee = fee
        self.capacity = capacity
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

    def check_capacity(self, capacity):
        for num_of_guests in capacity:
            if num_of_guests <= capacity:
                return "Enter!"
            else:
                return "Room too Full!"

























    








   