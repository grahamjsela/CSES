#  Find a missing number in a string of 1 to n numbers.
# I take in the n of the n numbers, and the string of the numbers 1 -n
# The script splits the string on the whitespace, and places each number into its
# own index in an array. To find the missing number, the script goes through the array 
# and returns the index where the number is 0. 

def main():

    n = int(input())

    arr = [0] * (n)
    i = 1

    temp = input().split()

    for el in temp:
        k = int(el)
        arr[k - 1] = k
        i = i + 1

    count = 1
    for element in arr:

        if element == 0:
            print(count)
            return

        count = count + 1

        

if __name__ == "__main__":
    main()
    