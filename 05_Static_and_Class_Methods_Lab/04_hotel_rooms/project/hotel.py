from project.room import Room
from typing import List

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        r = next((room for room in self.rooms if room.number == room_number), None)
        if r is not None:
            if r.capacity >= people and not r.is_taken:
                self.guests += people
                r.take_room(people)

    def free_room(self, room_number):
        r = next((room for room in self.rooms if room.number == room_number), None)
        if r is not None and r.is_taken:
            self.guests -= r.guests
            r.free_room()

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
                f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}\n")
