import sys

def sum_till_ones(number):
    output = 0

    for symb in str(number):
        output += int(symb)

        if output >= 10:
            temp_out = 0
            deconst = str(output)

            for i in deconst:
                temp_out += int(i)

            output = temp_out

    print(output)

if __name__ == '__main__':
    try:
        sum_till_ones(sys.argv[1])
    except IndexError:
        user_number = input('Введите число:\n')
        sum_till_ones(user_number)
