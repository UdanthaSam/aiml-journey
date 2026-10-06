import csv


temperature = input("Enter the temperature : ")
con = input("Which conversion do you need? Celsius to Fahrenheit (1) or Fahrenheit to Celsius (2): ")
if con == "1":
    celsius = float(temperature)
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif con == "2":
    fahrenheit = float(temperature)
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")


file = open("text.txt", "a+")
file.write("Hello")
text = file.read()
word = text.split()

print("Number of words in the file:", len(word))

exp = True
while exp == True:
    des = input("Enter the description of the expense: ")
    amount = input("Enter the amount of the expense: ")

    with open("expense.csv","a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([des, float(amount)])
        
    choice = input("Add another? (yes/no): ")
    if choice.lower() == "no":
        exp = False

pass