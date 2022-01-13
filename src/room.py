class Room:
    def __init__(self, name):
        self.name = name
        self.capacity = []
        self.songs = []

    def check_in_guest_to_room(self, guest):
        self.capacity.append(guest)
