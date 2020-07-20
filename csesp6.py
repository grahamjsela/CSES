# Problem:
#A number spiral is an infinite grid whose upper-left square has number 1 and goes around in a square incrementing each time.
# The following is an example number spiral of 5 x 5.
# 1  2  9  10 25
# 4  3  8  11 24
# 5  6  7  12 23
# 16 15 14 13 22
# 17 18 19 20 21
# The solution will find the number in row x and column y.

# Solution:
# Because of the nature of the number spiral, having squares on every second indice.
# My solution uses the larger number squares it and either subtracts or adds either,
# the row or column to it depending on which is larger. 
def main():

    t = int(input())
    num = 0

    for i in range(t):

        arr = input().split()
        y = int(arr[0])
        x = int(arr[1])

        if y > x:

            if y % 2 == 1:
                num = (y-1) * (y-1) + x
            else:
                num = y * y - x + 1
        else:
            
            if x % 2 == 1:
                num = x * x - y + 1
            else:
                num = (x-1) * (x-1) + y

        print(num)



if __name__ == "__main__":
    main()