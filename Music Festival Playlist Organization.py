# Task 1: Artist Lineup Compilation
# You are provided with a list of artist names scheduled to
# perform at different stages of the music festival. Using a 
# loop, compile these artist names into a set to create a unique 
# lineup without duplicates.

# Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
# unique_artists = set()
# Expected Outcome:
# A set containing unique artist names, such as 
# {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

def rmv_duplicates(lineup):
    
    unique = set()
    
    for artist in lineup:
        
        unique.add(artist)
        
    return unique

print(rmv_duplicates(artist_names))



# Task 2: Genre Sorting
# You have a list of genres associated with each artist. 
# Using a loop with sets, categorize artists by their genres, 
# creating a set for each genre.

# Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock",
    "Billie Eilish" : "Pop"
}
# Expected Outcome:
# A categorization of artists by genres, such as
# Genre: Folk, Artists: The Lumineers.

def genres(artists_genres):
    catergorized = {}
    
    for artist, genre in artists_genres.items():
        if genre in catergorized:
       
            catergorized[genre].add(artist)
        else:
            
            catergorized[genre] = {artist} #makes a dictionary of sets
            
    return catergorized

print(genres(artists_genres))


# Task 3: Playlist Duplication Check
# Create a Python script that takes multiple playlist sets 
# and checks if any playlist is a duplicate of another 
# (i.e., contains the same set of songs).

# Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]
# Expected Outcome:
# A confirmation of whether there are duplicate playlists, such as 
# Duplicate playlists found: True.

def dup_playlist(playlists):
    for i in range(len(playlists)):
        for j in range(i + 1, len(playlists)):
            
            if playlists[i] == playlists[j]:
                return True  
    return False

print(dup_playlist(playlists))