# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
# create varialbles for each item
broccoli =2
leek = 2
potato = 3
brussel_sprout = 7

#calculate total cost of buying one of each
sum_one_each = broccoli + leek + potato + brussel_sprout

#calculate average price per item
avg_price = sum_one_each / 4

#create variables for number of items wanted
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

#calculate total cost of all items
sum_total = (num_potatoes * potato) + (num_broccolis * broccoli) + (num_leeks * leek) + (num_brussel_sprouts * brussel_sprout)

# create variable for discount percentage
discount_percentage = 30

#calculate discount total
discounted_sum_total = sum_total - (sum_total * discount_percentage/100)

#round discount total to nearest cent
discounted_sum_total = round(discounted_sum_total, 2)

#print final amount
print (discounted_sum_total)









