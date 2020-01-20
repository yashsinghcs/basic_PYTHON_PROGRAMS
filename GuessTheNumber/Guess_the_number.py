import random


def game():
    a = random.choice(range(200))
    count = 0
    while True:
        try:
            k = int(input("guess the number (IN RANGE OF 200 )="))
            if a == k:
                print("CONGRATS YOOU WON\n", "\t IN", count, "STEPS\n")
                break
            elif k > a:
                print("guess smaller number than this \n")
                count += 1
            else:
                print("guess greater no than this \n")
                count += 1
        except:
            print("error handled try again ")


game()
