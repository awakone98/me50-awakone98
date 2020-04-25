#include cs50 
#include get_float

from cs50 import get_float

def main():
    change = get_change_owed("changed owed: ")
    cents = dollars_to_cents(change)
    print(cents_to_coins(cents))

#User input
def get_change_owed(prompt):
    while True:
        n = get_float(prompt)
        if 0 < n:
            break
    return n

def dollars_to_cents(amount):
    change = round(amount * 100)
    return change

def cents_to_coins(cents):
    q = cents // 25
    d = (cents % 25) // 10
    n = ((cents % 25) % 10) // 5
    p = ((cents % 25) % 10) % 5
    return q + d + n + p

if __name__ == "__main__":
     main()
#source https://www.youtube.com/watch?v=3NsWmAXhzU4