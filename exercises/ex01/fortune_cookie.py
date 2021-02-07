"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

from random import randint


number: int = ((randint(1, 4)))

if number == 1:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if number == 2:
        print("Your life will be happy and peaceful.")
    else:
        if number == 3:
            print("Soon life will become more interesting.")
        else:
            if number == 4:
                print("You are already on the right path to happiness and success.")

print("Now, go spread positive vibes!")
