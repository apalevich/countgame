import sys

def sum_till_ones(number):
    #create name for adding digits
    output = 0

    #add digits to the name one by one
    for symb in str(number):
        output += int(symb)

    #check if sum of the digits contains more than one digits
    if output >= 10:
        sum_till_ones(output)

    #print or return answer when it represented by one digit
    else:
        print(output)

if __name__ == '__main__':
    try:
        sum_till_ones(sys.argv[1])
    except IndexError:
        user_number = input('Введите число:\n')
        sum_till_ones(user_number)
