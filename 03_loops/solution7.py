# validate input
# Keep  asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter any Number to play Guess game: "))

    if 1 <= number <= 10:
        print(f"Congratulations you guessed {number}")
        break
    else:
        print("Sorry, Try again!")