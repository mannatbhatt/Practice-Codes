import random
import webbrowser
# Jumbled words and their correct answers
jumbled_words = {
    "ORNSTG": "STRONG",
    "CMORI": "MICRO",
    "HTAP": "PATH",
    "SSCUSCE": "SUCCESS",
    "NACOE": "OCEAN",
}
# To display jumbled words
print("Welcome to the Jumbled Word Puzzle!")
print("Unscramble the following words:")

# To Shuffle the word order
jumbled_word_keys = list(jumbled_words.keys())
random.shuffle(jumbled_word_keys)

# Declaring a dictionary to store user's answers
user_answers = {}

# Display jumbled words and get user input
for word_key in jumbled_word_keys:
    jumbled_word = word_key
    correct_answer = jumbled_words[word_key]

    user_input = input(f"\nUnscramble: {jumbled_word}\nYour Answer: ").upper()

    # Check user's answer
    if user_input == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
    
    # To store user answers in the dictionary
    user_answers[jumbled_word] = user_input

# The End
print("WELL DONE!!!")
start_button = input("Enter COMPLETE ")

if start_button.upper() == "COMPLETE":
    video_url = "https://i.pinimg.com/originals/1c/36/47/1c3647552cdd47b9935ada21746f6872.gif"  
    webbrowser.open(video_url)
else:
    print("Apologies for inconvenience!")
