import random
import time
import os
import sys
import itertools

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinning_cursor(duration=2):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\rRolling the die... {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.15)
    print("\r", end="")

def rolling_animation():
    clear()
    spinning_cursor()       
    dice_faces = [
        "[     ]\n[  o  ]\n[     ]",   # 1
        "[o    ]\n[     ]\n[    o]",   # 2
        "[o    ]\n[  o  ]\n[    o]",   # 3
        "[o   o]\n[     ]\n[o   o]",   # 4
        "[o   o]\n[  o  ]\n[o   o]",   # 5
        "[o   o]\n[o   o]\n[o   o]"    # 6
    ]

    for _ in range(10):
        clear()
        face = random.choice(dice_faces)
        print("Rolling...\n")
        print(face)
        time.sleep(0.2)

def roll_die():
    rolling_animation()
    result = random.randint(1, 6)
    face = {
        1: "[     ]\n[  o  ]\n[     ]",
        2: "[o    ]\n[     ]\n[    o]",
        3: "[o    ]\n[  o  ]\n[    o]",
        4: "[o   o]\n[     ]\n[o   o]",
        5: "[o   o]\n[  o  ]\n[o   o]",
        6: "[o   o]\n[o   o]\n[o   o]"
    }
    clear()
    print(f"You rolled a {result}!\n")
    print(face[result])

if __name__ == "__main__":
    first = True
    while True:
        if first:
            input("Press Enter to roll the die...")
            first = False
        roll_die()
        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
