# this is a comment.
print("Hello World!") #This will print result
name="jayesh"
age=21
coder=True
p=7
if(p>5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

icecream="Vanilla" # global variable
def foods():  #this is a function
    vegetable="potato"
    fruit="mango"
    print(vegetable+" is a local variable value.")
foods()
""" variable is outside the function but this is shown in result
    because icecream is global variable"""
print(icecream+" is a global variable value.")
# variable is outside the function that's why it is not shown in result
#print(fruit+" is a local variable value.")