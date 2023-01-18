# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')


order = 'leek 4'
number = int(order[order.find(" ")+1:])
sum_total = number * leek_price
print(sum_total)

broccoli_price = 2.34
order = 'broccoli 1.6'

weight = float(order[order.find(" ")+1:])

total_price = weight * broccoli_price
total_price = round(total_price,2)

print(str(weight) + 'kg broccoli costs ' + str(total_price) + 'e') 

