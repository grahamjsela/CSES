# Problem:
# You are given a DNA sequence: a string consisting of characters 
# A, C, G, and T. Your task is to find the 
# longest repetition in the sequence. This is a maximum-length 
# substring containing only one type of character.

#The script takes input and sets a temporary count to 1 for when there is no
#match but there would still be one in that length. The highest is set at 0 
# because nothing ahs been matched yet. And lastlet is a letter not included
# in the given alphabet. 
# The script then goes through each char in the input string and checks it against
# the previous letter seen. If they are the same then the temporary count is
# incremented and if it is not then temp is reset. If the temp is at any point bigger 
# than the highest count then high becomes temp. At the end we print the high.


def main():
    
    dna = input()

    high = 0
    temp = 1
    lastlet = 'z'

    for char in dna:
        
        if lastlet == char:
            temp = temp + 1
        else:
            lastlet = char
            temp = 1

        if temp > high:
            high = temp

    print(high)


if __name__ == "__main__":
    main()