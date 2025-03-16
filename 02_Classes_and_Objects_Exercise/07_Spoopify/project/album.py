from project.song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = songs
        self.published = False
        self.songs_list: list = []
        for song in self.songs:
            self.songs_list.append(song)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."  #possible problem here if both single and published
        if song in self.songs_list:
            return f"Song is already in the album."
        self.songs_list.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        s = next((song for song in self.songs_list if song.name == song_name), None)
        if self.published:
            return f"Cannot remove songs. Album is published."
        if s is None:
            return f"Song is not in the album."
        #possible problem here if both single and published
        self.songs_list.remove(s)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + '\n'.join([f'== {song.get_info()}' for song in self.songs_list])
