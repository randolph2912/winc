# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

def alphabetical_order(films):
    print("Sorted Films: ", sorted(films))
    return sorted(films)

def won_golden_globe(film):
    golden_globe_winners = [
        "Jaws", "Star Wars", "Close Encounters of the Third Kind",
        "Superman", "E.T. the Extra-Terrestrial", "Jurassic Park",
        "Schindler's List", "Saving Private Ryan", "Memoirs of a Geisha"
    ]
    print("Golden Globe Winner: ", film.lower() in [winner.lower() for winner in golden_globe_winners])
    return film.lower() in [winner.lower() for winner in golden_globe_winners]

def remove_toto_albums(films):
    toto_albums = [
        "Hydra", "Turn Back", "IV", "Isolation",
        "Toto XIV", "The Seventh One", "Fahrenheit",
        "Kingdom of Desire", "Tambu", "Old Is New", "Mindfields"
    ]
    print("Films not matching Toto Albums: ", [film for film in films if film.lower() not in [album.lower() for album in toto_albums]])
    return [film for film in films if film.lower() not in [album.lower() for album in toto_albums]]















