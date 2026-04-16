from cs50 import get_float

cents = get_float("Change owed: ")  #prompt the user for the amount of change owed
while cents < 0:
    cents = get_float("Change owed: ")  #keep prompting the user until they provide a valid amount of change (non-negative)
cents = int(cents * 100)  #convert the amount of change from dollars to cents to avoid floating-point precision issues

coins = 0

coins += cents // 25
cents = cents % 25

coins += cents // 10
cents = cents % 10

coins += cents // 5
cents = cents % 5

coins += cents // 1

print(f"{coins}") 
