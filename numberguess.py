print("This is a game for guessing a number between 1 and 10. If you guess the exact number, the game will stop.")
a = int(input("Enter the number that you guessed."))
while(a!=5):
    a=int(input("Your previous guess was wrong. Try again."))

print("Eureka! Your guess was right. The number was 5")

