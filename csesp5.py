# Problem:
# A permutation of integers 1,2,…,n is called beautiful
# if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.

# Solution:
# A beautiful permutation can be completed on all numbers except 2 and 3.
# So my solution first handles for the case that 2 or 3 is inputed.
# Next my solution puts all even numbers from increasing values 2 to n or n - 1.
# And follows that up with all odd numbers from 1 to n or n-1 and creates a beautiful permutation.

def main():

    n = int(input())
    num = 0

    if n == 2 or n == 3:
        print("NO SOLUTION")
        exit

    for i in range(n):

        num = num + 2

        if num > n:
            num = 1
        
        print(num)



if __name__ == "__main__":
    main()