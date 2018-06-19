word = input("Type a word for someone to guess:\n")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
while (word.isalpha() == False):
	print("That's not a word!")
	word = input()
answer = []

for i in range(len(word)):
	answer.append("_")


print(answer)

# Some useful variables
guesses = []
maxfails = 7

guess = input("Guess a letter: ")
