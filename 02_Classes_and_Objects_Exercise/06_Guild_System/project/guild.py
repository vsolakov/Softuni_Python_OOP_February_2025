from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        player = next((p for p in self.players if p.name == player_name), None)
        if player is None:
            return f"Player {player_name} is not in the guild."
        else:
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player.name} has been removed from the guild."

    def guild_info(self):
        result = (f"Guild: {self.name}\n"
                  + '\n'.join(p.player_info() for p in self.players))
        return result

