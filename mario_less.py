import cs50   #for the get_int function


height = cs50.get_int("Height: ")   #prompt the user for the height of the pyramid
while height < 1 or height > 8:       #keep prompting the user until they provide a valid height (between 1 and 8)
    height = cs50.get_int("Height: ")   #prompt the user for the height of the pyramid again if the previous input was invalid


for i in range(height):
    print(" " * (height - i - 1) + "#" * (i + 1)) # " " * (height - i - 1) this meanss ki repeat the first one for seecond one times
