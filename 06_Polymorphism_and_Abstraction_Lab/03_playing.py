class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(instance):
    return instance.play()


guitar = Guitar()
print(start_playing(guitar))
