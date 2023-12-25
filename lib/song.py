class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.update_genre_count(genre)
        Song.update_artist_count(artist)

    @classmethod
    def update_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre]+= 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def update_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist]+= 1
        else:
            cls.artist_count[artist] = 1

  
