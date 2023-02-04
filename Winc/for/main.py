from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


def shortest_names(countries):
    shortest = min(len(country) for country in countries)
    return [country for country in countries if len(country) == shortest]

def most_vowels(countries):
    vowels = 'aeiouAEIOU'
    country_vowels = [(country, sum(1 for letter in country if letter in vowels)) for country in countries]
    country_vowels.sort(key=lambda x: x[1], reverse=True)
    return [country[0] for country in country_vowels[:3]]

def alphabet_set(countries):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    for country in countries:
        alphabet -= set(country.lower())
        if not alphabet:
            break
    return [country for country in countries if set(country.lower()).issubset(set('abcdefghijklmnopqrstuvwxyz') - alphabet)]

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))
