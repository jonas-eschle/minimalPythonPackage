from examplepkg.humans import Artist


class Zoo:
    def __init__(self, name):
        self.name = name
        self.artists = []
        self.add_artist(Artist("Bob Ross"))

    def add_artist(self, artist):
        self.artists.append(artist)

    def __str__(self):
        return f"{self.name} Zoo has {len(self.artists)} artists"
