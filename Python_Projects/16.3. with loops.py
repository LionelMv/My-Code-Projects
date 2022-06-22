secret_name = "Eva"
user_input = ""
limit = 3
count = 0
out_of_tries = False

while user_input != secret_name and not (out_of_tries):
    if count < limit:
        user_input = input("Enter the secret name: ")
        count += 1

    else:
        out_of_tries = True

if out_of_tries:
    print("Too many tries. Who the fuck are you?")
else:
    print("Hello beautiful. You are awesome.")