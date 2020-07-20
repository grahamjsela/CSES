#Problem:
#You are given an array of n integers. 
# You want to modify the array so that it is increasing, 
# i.e., every element is at least as large as the previous element.
# On each turn, you may increase the value of any element by one. 
# What is the minimum number of turns required?

# My solution goes through the array once to save on time. The solution 
# goes through the array individually and takes the largest number before it
# and adds that to a variable that stores how many total turns it will take.
# Each step the algorithm checks to see if it is using the largest number then
# the algorithm increases the count if it needs to.
def main():
    n = int(input())

    arr = list(map(int,input().split()))


    i = 0
    count = 0
    
    max = 0

    for i in range(n):

        if arr[i] > max:
            max = arr[i]

        if arr[i] < max:
            count = count + max - arr[i]

    print(count)
            
        
        

    




if __name__ == "__main__":
    main()