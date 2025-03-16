from project.album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        a = next((album for album in self.albums if album.name == album_name), None)
        if a is None:
            return f"Album {album_name} is not found."
        if a.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(a)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n" + "\n".join([f'{album.details()}' for album in self.albums])
        return result