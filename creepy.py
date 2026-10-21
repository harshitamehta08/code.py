import time
import random

message=[
    "a ghost is watching you"
    "don't look behind you"
    "someone is in your room"
    "i can see you"
    "the ghost is comming..."
]
print("welcome to the haunted terminal")
time.sleep(1)

for i in range(5):
    message=random.choice(message)

    for char in message:
        print(char, end="",flush=True)
        time.sleep(0.08)

        print()
        time.sleep(1)

        print("\n booooo! happy halloween!")