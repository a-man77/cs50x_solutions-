import cs50

string = input("Text: ")

letters = 0
words = 0
sentences = 0

length = len(string)

for i in range(length):
    if string[i].isalpha():
        letters += 1
    elif string[i].isspace():
        words += 1
    elif string[i] in [".", "!", "?"]:
        sentences += 1

words += 1
L = (letters / words) * 100
S = (sentences / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8

grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
