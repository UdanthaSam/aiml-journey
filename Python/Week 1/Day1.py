### Python Day 1 - Basics

# 1. Print statements

print("You've successfully run some Python code")
print("Congratulations!")


# 2. Variables and strings

color = "blue"

print("My favorite color is:", color)


# 3. Basic arithmetic

pi = 3.14159
diameter = 3

# Radius is half of the diameter
radius = diameter / 2

# Area of a circle = pi * radius squared
area = pi * (radius ** 2)

print("Radius:", radius)
print("Area:", area)


# 4. Swapping variables

a = [1, 2, 3]
b = [3, 2, 1]

print("Before swapping:")
print("a =", a)
print("b =", b)

z = a
a = b
b = z

print("After swapping:")
print("a =", a)
print("b =", b)


# 5. Arithmetic with parentheses

result_1 = (5 - 3) // 2

print("Result 1:", result_1)


# Expression that evaluates to 0
result_2 = (8 - 3) * (2 - (1 + 1))

print("Result 2:", result_2)


# 6. Candy sharing using modulus

alice_candies = 121
bob_candies = 77
carol_candies = 109

total_candies = alice_candies + bob_candies + carol_candies

to_smash = total_candies % 3

print("Total candies:", total_candies)
print("Candies to smash:", to_smash)


# 7. Basic arithmetic operator examples

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("True division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Negation:", -a)





### Python Day 2 - Functions and Built-in Functions

# 1. Round a number to two decimal places

def round_to_two_places(num):
    return round(num, ndigits=2)


print(round_to_two_places(3.14159))
# Output: 3.14


# 2. Using negative ndigits with round()

number = 3456

print(round(number, ndigits=-1))   # 3460
print(round(number, ndigits=-2))   # 3500
print(round(number, ndigits=-3))   # 3000


# 3. Candy sharing function

def to_smash(total_candies, friend_count=3):
    """
    Return the number of leftover candies after dividing
    the candies equally among the specified number of friends.

    If friend_count is not provided, 3 friends are assumed.
    """
    return total_candies % friend_count


print(to_smash(91))
# Output: 1

print(to_smash(91, 4))
# Output: 3


# 4. Practice - Rounding

def round_number(x):
    return round(x, ndigits=3)


print(round_number(9.9999))
# Output: 10.0


# 5. Finding the smallest absolute value

x = -10
y = 5

smallest_abs = min(abs(x), abs(y))

print(smallest_abs)
# Output: 5


# 6. Using abs() inside a function

def absolute_value(x):
    y = abs(x)
    return y


print(absolute_value(-5))
# Output: 5



### Python Day 3 - Lists and Loops
# Python Day 3 - Booleans and Conditionals


# 1. Sign function

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print(sign(10))    # 1
print(sign(-5))    # -1
print(sign(0))     # 0


# 2. Candy grammar using conditionals

def to_smash(total_candies):
    """
    Return the number of leftover candies after distributing
    the candies evenly between 3 friends.
    """

    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")

    return total_candies % 3


print(to_smash(91))
print(to_smash(1))


# 3. Weather condition example

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    """
    Return whether the person is prepared for the weather.
    """

    return (
        have_umbrella
        or (rain_level < 5 and have_hood)
        or not (rain_level > 0 and is_workday)
    )


print(prepared_for_weather(False, 6.0, False, False))


# 4. Simple boolean function

def is_negative(number):
    return number < 0


print(is_negative(-10))   # True
print(is_negative(5))     # False


# 5. Hot dog topping conditions


# Customer does not want onion

def onionless(ketchup, mustard, onion):
    return not onion


print(onionless(True, True, False))


# Customer wants all toppings

def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion


print(wants_all_toppings(True, True, True))
print(wants_all_toppings(True, False, True))


# Customer wants no toppings

def wants_plain_hotdog(ketchup, mustard, onion):
    return not ketchup and not mustard and not onion


print(wants_plain_hotdog(False, False, False))
print(wants_plain_hotdog(True, False, False))


# Customer wants ketchup or mustard, but not both

def exactly_one_sauce(ketchup, mustard, onion):
    return ketchup != mustard


print(exactly_one_sauce(True, False, False))
print(exactly_one_sauce(True, True, False))


# 6. Exactly one topping

def exactly_one_topping(ketchup, mustard, onion):
    """
    Return True if exactly one topping is selected.
    """

    return int(ketchup) + int(mustard) + int(onion) == 1


print(exactly_one_topping(True, False, False))
print(exactly_one_topping(True, True, False))
print(exactly_one_topping(False, False, False))


# 7. Boolean and integer conversion

print(int(True))     # 1
print(int(False))    # 0

print(bool(1))       # True
print(bool(0))       # False


# 8. Basic Blackjack decision function

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """
    Return True if the player should request another card.

    Simple strategy:
    - Hit when player total is below 17.
    - Stay when player total is 17 or higher.
    """

    return player_total < 17


print(should_hit(10, 14, 0, 0))   # True
print(should_hit(10, 18, 0, 0))   # False


### Day 4 
# Python Day 4 - Lists


# 1. Select the second element from a list

def select_second(L):
    """
    Return the second element of the given list.
    If the list has no second element, return None.
    """
    if len(L) < 2:
        return None

    return L[1]


print(select_second([10, 20, 30]))   # 20
print(select_second([10]))           # None


# 2. Get the captain of the worst team

def losing_team_captain(teams):
    """
    Return the captain of the last team in the list.
    The captain is the second person in each team.
    """
    return teams[-1][1]


teams = [
    ["Coach A", "Captain A", "Player A"],
    ["Coach B", "Captain B", "Player B"],
    ["Coach C", "Captain C", "Player C"]
]

print(losing_team_captain(teams))
# Captain C


# 3. Swap the first and last racer

def purple_shell(racers):
    """
    Swap the first-place racer with the last-place racer.
    """
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp


racers = ["Mario", "Bowser", "Luigi"]

purple_shell(racers)

print(racers)
# ['Luigi', 'Bowser', 'Mario']


# 4. List lengths

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

lengths = [
    len(a),
    len(b),
    len(c),
    len(d)
]

print(lengths)
# [3, 2, 0, 2]


# 5. Fashionably late guest

def fashionably_late(arrivals, name):
    """
    Return True if the guest arrived after at least half
    of the guests, but was not the final guest.
    """
    position = arrivals.index(name)

    return position >= len(arrivals) / 2 and position != len(arrivals) - 1


party_attendees = [
    "Adela",
    "Fleda",
    "Owen",
    "May",
    "Mona",
    "Gilbert",
    "Ford"
]

print(fashionably_late(party_attendees, "Mona"))      # True
print(fashionably_late(party_attendees, "Gilbert"))   # True
print(fashionably_late(party_attendees, "Ford"))      # False
print(fashionably_late(party_attendees, "Adela"))     # False