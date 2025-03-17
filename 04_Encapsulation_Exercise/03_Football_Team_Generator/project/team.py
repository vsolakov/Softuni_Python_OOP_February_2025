from project.player import Player
from typing import List

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        p = next((player for player in self.__players if player.name == player_name), None)
        if p is not None:
            self.__players.remove(p)
            return p
        return f"Player {player_name} not found"