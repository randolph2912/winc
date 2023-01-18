# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# soccer match information
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_1 + ' ' + str(goal_0) + ', ' + scorer_2 + ' ' + str(goal_1)
report = f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"

#player information
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
if ' ' in player:
    last_name_len = len(player[player.rfind(' ')+1:])
else:
    last_name_len = 0    
name_short = player[0] + '. ' + player[player.find(' ')+1:]
chant = first_name + '!'
chant = ' '.join([chant]*len(first_name)) 
if len(chant)>0:
    good_chant = chant [-1] != ' '
else:
    good_chant = False

print(scorers)
print(report)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
