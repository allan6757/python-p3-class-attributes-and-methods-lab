class Song:
    # Class Attributes
    # These are shared by all Song objects
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, title, artist, genre):
        # Instance Attributes
        # These are unique to each Song object
        self.name = title
        self.artist = artist
        self.genre = genre

        # Update the class attributes whenever a new Song is created
        Song.count += 1

        if genre not in Song.genres:
            Song.genres.append(genre)

        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update genre count
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Update artist count
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
