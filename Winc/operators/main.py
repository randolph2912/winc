# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# The language spoken the most in switzerland is the same as in spain.
spain_primary_language = "Spanish"
switzerland_primary_language = "German"
print(spain_primary_language == switzerland_primary_language)

#the most prevalent religion in switzerland is the same as in spain .
spain_primary_religion = "Roman Catholic"
switzerland_primary_religion = "Roman Catholic"
print(spain_primary_religion == switzerland_primary_religion)

#The name lenght of spain's capital does not equal that of switzerland.
spain_capital = "madrid"
switzerland_capital = "Bern"
print(len(spain_capital) !=len(switzerland_capital))

#Switzerland's GDP is greater than Spain's GDP.
spain_gdp = 1.3
switzerland_gdp = 0.6
print(spain_gdp < switzerland_gdp)

#The population growth is less than 1% in Switzerland and spain. 
spain_pop_growth = 0.5
switzerland_pop_growth = 0.1
print(spain_pop_growth < 1 and switzerland_pop_growth < 1)

#At least one of the two countries has a population count of over 10 million.
spain_pop = 47000000
switzerland_pop = 8600000
print(spain_pop > 10000000 or switzerland_pop > 10000000)

#Exactly one of the two countries has a population count of over 10 million.
print((spain_pop > 10000000 and switzerland_pop <= 10000000) or (spain_pop <= 10000000 and switzerland_pop > 10000000))
