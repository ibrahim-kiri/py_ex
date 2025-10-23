# simple countdown timer using a while loop.
import time

def countdown_timer(seconds):

    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1) # Pause for 1 second
        seconds -= 1

    print("Time's up!")

# Get the countdown duration from the user
duration = 5
countdown_timer(duration)
