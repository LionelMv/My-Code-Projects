secret_word = "Eva"
secret_input = ""
guess_count = 0
limit = 2
out_of_guesses = False

while secret_input != secret_word and not (out_of_guesses):
    if guess_count <= limit:
        secret_input = input("Enter the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses. You lose!")
else:
    print("You win!")