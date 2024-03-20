

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

user_mood = input("How are you feeling today?")
if user_mood == "happy":
    print("That's great to hear!")
elif user_mood == "sad":
    print("I hope your day gets better!")

pi_value = 3.14
user_age = 25
user_location = "New York"
max_limit = 1000

variable_a = ("Hello, World!") #string datatype
print(variable_a)
print(type("variable_a"))
variable_b = 23 #integers
print(variable_b)
print(type("variable_b"))
variable_c = 3.14 #floats 
print(variable_c)
print(type("variable_c"))
variable_d = True #boolean variable
print(variable_d)
print(type("variable_d"))

# units are in dollars
ice_cream = 3
chocolate_cake = 12
apple_pie = 5
total_cost = ice_cream + chocolate_cake + apple_pie
print(total_cost)

savings = 10000.00
interests = 0.07
expected_outcome = (savings*interests) + savings
print(expected_outcome)

a = 5
b = 3
a, b = b, a
print(a)
print(b)