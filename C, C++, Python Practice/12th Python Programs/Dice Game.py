import random
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘
#https://youtu.be/x-Ag2_bJ40Y?si=yfGK5HqH6kIyF_Po  - TRY last part from here

"┌─────────┐"
"│                       │ "
"│                       │ "
"│                       │"
"└─────────┘ "

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

print(f"Total = {total}") 

for die in range(n):
    for line in dice_art.get(dice[die]):  #to print value (dice pattern) from given key(dice) 
                                                                      #where dice is a list and die are keys for the values to be printed, i.e [1,2,3,4,5,6]
         print(line)                            
