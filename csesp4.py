#Problem:
#You are given an array of n integers. 
# You want to modify the array so that it is increasing, 
# i.e., every element is at least as large as the previous element.
# On each turn, you may increase the value of any element by one. 
# What is the minimum number of turns required?

def main():
    n = int(input())

    arr = list(map(int,input().split()))


    i = 0
    max = 0
    temp = 0
    

    if n == 0:

        print(0)
        return

    while(i < n - 1):

        if (arr[i + 1] < arr[i]):

            temp = arr[i] - arr[i + 1] + 1

            if temp > max:

                max = temp

        temp = 0
        i = i + 1

    print(max)

    




if __name__ == "__main__":
    main()