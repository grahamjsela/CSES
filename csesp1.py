#Very simple python script
# Takes an input, and checks to see if it is = to 1
# if it is, it prints 1 then ends the program.
# Otherwise, the script checks whether the number is even or odd.
# In the case of odd, the number is multiplied by 3 and added 1.
# In the case of even, the number is divided by two.
# This process takes place until the number is equal to 1. In which case the program is ended.
def main():
    
    n = int(input())
    
    print(n)

    if n ==1:
        return

    while (n != 1):

        if n % 2 == 1:
            n = n * 3 + 1
            print(int(n))

        else:
            n = n / 2
            print(int(n))
    
    return
    

if __name__ == "__main__":
    main()