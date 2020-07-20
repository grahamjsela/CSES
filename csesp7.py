
def main():

    count = 0
    n = int(input())
    minus = 0
    
    for i in range(1,n+1):

        k = i * i
        prev = (i-1) * (i-1)

        count = count + sum(range(prev,k))
        
        count = count - minus
        minus = (8 * (i - 1))
        print(count)
        

    

if __name__ == "__main__":
    main()