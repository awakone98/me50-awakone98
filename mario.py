#include cs50
#include get_int
from cs50 import get_int

def main():
    height = get_height("height: ")
    draw_half_pyramid(height)

def get_height(prompt):
    while True:
     height = get_int(prompt)
     #input between 1 and 8 (inclusive)
     if height > 0 and height < 9:
        break
    return height

def draw_half_pyramid(rows):
    #start each row at one 
    #increase each row by one
    for row in range(1, rows + 1):
        #print half a pyramid with hashtags and space
        print(" " * (rows - row) + "#" * row)

if __name__ == "__main__":
     main()
#source https://www.youtube.com/watch?v=3NsWmAXhzU4

    
