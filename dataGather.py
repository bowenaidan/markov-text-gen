import lyricsgenius as lg
file = open("lyrics.txt", "w")

genius = lg.Genius('Key', skip_non_songs=True, 
                   excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def retrieveLyrics(array, k):
    count = 0
    for name in array:
        try:
            songs = genius.search_artist(name, max_songs=k, sort='popularity').songs
            for song in songs:
                # Remove the first line of lyrics
                song_lyrics = song.lyrics.split('\n', 1)[-1]
                file.write(song_lyrics + "\n \n    \n \n")
            count += 1
            print(f"{len(songs)} songs retrieved.")
        except:
            print(f"Exception caught. Song: {len(songs)}.")
            continue

if __name__ == '__main__':
    array = ["Taylor Swift"]
    k = 10
    retrieveLyrics(array, k)
