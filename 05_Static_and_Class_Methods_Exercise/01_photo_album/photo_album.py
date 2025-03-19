from math import ceil
class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for index, element in enumerate(self.photos):
            if len(element) < 4:
                element.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(element)}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for row in range(len(self.photos)):
            for col in range(len(self.photos[row])):
                result += "[]"
                if col < (len(self.photos[row]) - 1):
                    result += " "
            result += "\n-----------\n"
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))


print(album.display())
