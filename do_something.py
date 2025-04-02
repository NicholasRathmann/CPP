def two_plus_two(number) -> int:
    if number < 0:
        return -1
    while True:
        if number == 2 + 2:
            return number
        elif number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1

def fibonachi_head():
    return 1

def attempt_to_sort(list_of_numbers):
    temp = list_of_numbers[0]
    list_of_numbers[0] = list_of_numbers[1]
    list_of_numbers[1] = temp
    max = list_of_numbers[0]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] >= max:
            max = list_of_numbers[i]
        else:
            return -1
    return list_of_numbers
        
        

if __name__ == '__main__':
    print("The first fibonacci number is " + str(fibonachi_head()))