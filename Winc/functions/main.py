# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return "Hello, " + name + "!"  

def add (num1, num2, num3) :
    return num1 + num2 + num3

def positive(num):
    return num > 0

def negative (num):
    return num < 0

name = "Randolph"   
print(greet(name))     

result = add(1, 2, 3)
print("the sum of 1, 2 and 3 is : ", result)

check = positive(5)
print("is 5 positive?", check)

check = negative(-5)
print("is -5 negative?", check)