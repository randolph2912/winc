# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
import json
from helpers import get_countries

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    return {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }

def add_stamp(passport, country):
    countries = get_countries()
    if passport.get("nationality") == country:
        return passport
    if passport.get("stamps") is None:
        passport["stamps"] = []
    if country not in passport["stamps"]:
        passport["stamps"].append(country)
    return passport

def add_biometric_data(passport, type, value, date):
    if "biometric" not in passport:
        passport["biometric"] = {}
    passport["biometric"][type] = {"value": value, "date": date}
    return passport
