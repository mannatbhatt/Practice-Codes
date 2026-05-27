import random
dice_art={
    1:("┌─────────┐",
        "│                       │ ",
        "│           ●          │",
        "│                       │" ,                   
        "└─────────┘ "),
    2:("┌─────────┐",
        "│ ●                    │",
        "│                       │",
        "│                    ● │",                    
        "└─────────┘"),
    3:("┌─────────┐",
        "│ ●                    │",
        "│          ●           │",
        "│                    ● │",                   
        "└─────────┘"),
    4:("┌─────────┐",
        "│ ●                ●  │",
        "│                       │",
        "│ ●                ●  │",                    
        "└─────────┘"),
    5:("┌─────────┐",
        "│ ●                ●  │",
        "│          ●           │",
        "│ ●                ●  │",                    
        "└─────────┘"),
    6:("┌─────────┐",
        "│      ●       ●      │",
        "│      ●       ●      │",
        "│      ●       ●      │" ,                   
        "└─────────┘")
    }

dice=[ ]
total = 0
n = int(input("How many dice? ")) #num_of_dice

for die in range(n):
    r = random.randint(1,6)
    dice.append(r)
    
print(dice)

for die in dice:
    total += die
                                                #By default, the print function ends with a newline.
print(f"Total = {total}")       #Passing the whitespace to the end parameter (end=' ') indicates that                   
                                       #the end character has to be identified by whitespace and not a newline.


for line in range(5):               #range = 5 because in tuple value, 5 lines are there, dice is made of 5 lines
    for die in dice:
        print(dice_art.get(die)[line], end=" ")      #.get(die) is number 1-6 and [line] is added as the dice will be formed by the loop of lines in the tuple value
    print( )                                                      #end character is " ", empty string
#a print statement is added outside of the inner loop
