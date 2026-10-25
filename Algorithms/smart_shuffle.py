import random

from pprint import pprint

# Case 1
# Exery artist has the exact same number of songs, in this example we're gonna have five songs per artist
# Case 2
# The artists doesn't have the same number os songs
# Case 3 
# We're gonne classify the artits based on the number of songs so the playlist are gonna have most of the artists with three or more and other with only
# one or two songs


class Song:
    def __init__(self, title: str, artist: str) -> None:
        self.title = title
        self.artist = artist

    def __repr__(self):
        return f"{self.title} from {self.artist}"

class SmartShuffle:
    def __init__(self, songs: list) -> None:
        self.songs = songs
        self.playlist = self.generate_playlist()

    def generate_playlist(self) -> list[Song]:
        """Runs a random shuffle on the songs and generate a playlist"""

        playlist = []

        # shuffle all the lists
        random.shuffle(self.songs)
        for artists in self.songs:
            random.shuffle(artists)

        len_songs = len(self.songs[0])
        len_artists = len(self.songs)

        for it_song in range(len_songs):
            for it_ar in range(len_artists):
                playlist.append(
                    self.songs[it_ar][it_song]
                )

        return playlist
                
                

def populate_songs(songs: dict) -> list[list[Song]]:
    """Generate a list of songs
    
    Attributes
    ----------
    songs : dict
        A dictionary where each key represents an artist and each value is a list of songs by that artist

    Returns
    -------
    list : list[Song]
        A two-dimensional list where each row is a list of songs by a specific artist.    
    """

    exit_list = []

    for key, items in songs.items():

        # Insert a list of songs sorted by artist in a specific way
        exit_list.append(
            [ Song(item, key) for item in items ]
        ) 

    return exit_list

if __name__ == "__main__":

    songs_dict = {
        "Nirvana": ["In bloom", "Love Buzz", "About a girl", "Lounge act", "You know you're right"],
        "Pearl Jam": ["Porch", "Oceans", "Even flow", "Black", "Daughter"],
        "Alice in chains": ["Would", "Angry chair", "Nutshell", "Sea of sorrow", "Grind"],
        "Soundgarden": ["Black hole sun", "Fell on black days", "Rusty cage", "Outshined", "Burden in my hand"]
    }
        
    songs = populate_songs(songs_dict)

    print(songs)

    smart_shuffle = SmartShuffle(songs)
    pprint(smart_shuffle.playlist)
