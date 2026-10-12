import csv

# ============================================================
# PYTHON PRACTICE NOTES
# Topics:
# - Lists
# - Strings
# - Dictionaries
# - External Libraries
# - Error Handling
# ============================================================


# ------------------------------------------------------------
# 1. LISTS
# ------------------------------------------------------------

# A list stores multiple values in one variable.
fruits = ["apple", "banana", "orange"]

# Access items using an index.
print(fruits[0])      # apple
print(fruits[-1])     # orange

# Get the number of items in the list.
print(len(fruits))

# Change an item in a list.
fruits[1] = "mango"
print(fruits)

# Add a new item.
fruits.append("grapes")
print(fruits)

# Find the position of an item.
print(fruits.index("orange"))


# ------------------------------------------------------------
# 2. NESTED LISTS
# ------------------------------------------------------------

# A list can contain other lists.
teams = [
    ["Coach A", "Captain A", "Player A"],
    ["Coach B", "Captain B", "Player B"]
]

# Access an item inside a nested list.
print(teams[1][1])    # Captain B


# ------------------------------------------------------------
# 3. STRINGS
# ------------------------------------------------------------

text = "Python is Fun"

# Get string length.
print(len(text))

# Convert to lowercase.
print(text.lower())

# Split a string into words.
words = text.split()
print(words)

# Check whether a string contains only digits.
number_text = "12345"
print(number_text.isdigit())

# Remove selected characters from the end.
word = "hello,"
clean_word = word.rstrip(",.")
print(clean_word)


# ------------------------------------------------------------
# 4. STRING CLEANING
# ------------------------------------------------------------

sentence = "Python is Great."

# Split sentence into words.
words = sentence.split()

# Convert words to lowercase and remove punctuation.
clean_words = []

for word in words:
    clean_word = word.rstrip(".,").lower()
    clean_words.append(clean_word)

print(clean_words)


# ------------------------------------------------------------
# 5. DICTIONARIES
# ------------------------------------------------------------

# Dictionaries store key-value pairs.
student = {
    "name": "John",
    "score": 85
}

# Access values using keys.
print(student["name"])
print(student["score"])

# Update a value.
student["score"] = 90

# Add a new key and value.
student["age"] = 20

print(student)

# Check whether a key exists.
if "name" in student:
    print("Name exists")


# ------------------------------------------------------------
# 6. COUNTING ITEMS USING A DICTIONARY
# ------------------------------------------------------------

items = ["apple", "banana", "apple", "orange", "apple"]

counts = {}

for item in items:

    # If item is not already in the dictionary,
    # create it with a starting count of 0.
    if item not in counts:
        counts[item] = 0

    # Increase the count.
    counts[item] += 1

print(counts)


# ------------------------------------------------------------
# 7. LIST OF DICTIONARIES
# ------------------------------------------------------------

racers = [
    {
        "name": "Peach",
        "items": ["banana", "green shell"],
        "finish": 3
    },
    {
        "name": "Bowser",
        "items": ["green shell"],
        "finish": 1
    }
]

# Access a value from the first dictionary.
print(racers[0]["name"])

# Access an item inside a list inside a dictionary.
print(racers[0]["items"][1])


# ------------------------------------------------------------
# 8. FUNCTIONS
# ------------------------------------------------------------

def greet(name):
    # Return a greeting using the supplied name.
    return f"Hello, {name}"


print(greet("John"))


# ------------------------------------------------------------
# 9. WORD SEARCH FUNCTION
# ------------------------------------------------------------

def word_search(documents, keyword):

    matches = []

    # enumerate() gives both the index and value.
    for index, document in enumerate(documents):

        # Split the document into individual words.
        words = document.split()

        cleaned_words = []

        for word in words:
            cleaned_word = word.rstrip(".,").lower()
            cleaned_words.append(cleaned_word)

        # Compare using lowercase so the search is case-insensitive.
        if keyword.lower() in cleaned_words:
            matches.append(index)

    return matches


documents = [
    "Python is easy.",
    "I like Java.",
    "Python is powerful."
]

print(word_search(documents, "python"))


# ------------------------------------------------------------
# 10. EXTERNAL LIBRARIES
# ------------------------------------------------------------

# Import the built-in math library.
import math

# Use a function from the library.
print(math.sqrt(25))

# Python tools that help inspect unfamiliar objects.
print(type(math))
print(dir(math))

# help() shows documentation for an object or function.
# Uncomment this if you want to view it.
# help(math.sqrt)


# ------------------------------------------------------------
# 11. BASIC TRY / EXCEPT
# ------------------------------------------------------------

try:
    age = int(input("Enter your age: "))

    print(f"You are {age} years old.")

except ValueError:
    # Runs if the input cannot be converted into an integer.
    print("Invalid age. Please enter a number.")


# ------------------------------------------------------------
# 12. MULTIPLE EXCEPT BLOCKS
# ------------------------------------------------------------

try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    # Happens when the user enters invalid numeric input.
    print("Invalid number.")

except ZeroDivisionError:
    # Happens when the second number is zero.
    print("Cannot divide by zero.")


# ------------------------------------------------------------
# 13. TRY / EXCEPT / ELSE
# ------------------------------------------------------------

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    # Runs only when no exception occurs.
    print("You entered:", number)


# ------------------------------------------------------------
# 14. TRY / EXCEPT / FINALLY
# ------------------------------------------------------------

try:
    pin = int(input("Enter PIN: "))

except ValueError:
    print("PIN must contain numbers only.")

finally:
    # finally always runs.
    print("Login attempt completed.")


# ------------------------------------------------------------
# 15. RAISING AN EXCEPTION
# ------------------------------------------------------------

try:
    age = int(input("Enter age: "))

    # Python allows negative integers,
    # but we can manually reject them.
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age accepted:", age)

except ValueError as error:
    print(error)


# ------------------------------------------------------------
# 16. HANDLING KEYERROR
# ------------------------------------------------------------

students = {
    "John": 78,
    "Sarah": 91,
    "Mike": 64
}

name = input("Enter student name: ")

try:
    print(f"{name} scored {students[name]}")

except KeyError:
    # Happens when the dictionary does not contain that key.
    print("Student not found.")


# ------------------------------------------------------------
# 17. HANDLING INDEXERROR
# ------------------------------------------------------------

fruits = ["Apple", "Banana", "Orange"]

try:
    index = int(input("Enter fruit index: "))

    print(fruits[index])

except ValueError:
    print("Please enter a number.")

except IndexError:
    # Happens when the index does not exist in the list.
    print("That position does not exist.")


# ------------------------------------------------------------
# 18. SIMPLE CALCULATOR WITH ERROR HANDLING
# ------------------------------------------------------------

try:
    first_number = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second_number = float(input("Enter second number: "))

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        result = first_number / second_number

    else:
        result = None
        print("Invalid operator.")

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    # Only print the result if a valid operator was used.
    if result is not None:
        print("Result:", result)

finally:
    print("Calculator closed.")





avg = 0
count = 0


with open("marks.csv") as file:
    reader = csv.reader(file)
    next (reader)  # Skip the header row

    for row in reader:
        print(row[1])
        avg = avg + int(row[1])
        count = count + 1
        print("Average", avg/count)

pass


with open("marks.csv") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        mark = row[2]
        avg = avg + int(mark)
        count = count + 1

        print(f"{name} scored {mark}")
    print("Average:", avg/count)
pass


x = "y"
with open("marks.csv","w",newline="") as file:
    writer = csv.writer(file)
    while x == "y":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        mark = int(input("Enter mark: "))
        writer.writerow([name,age,mark])
        x = input("Do you want to add another record? (y/n): ")
pass

with open("marks.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        name = row[0]
        age = row[1]
        mark = row[2]

        print(f"{name} is {age} years old and scored {mark}")
pass
