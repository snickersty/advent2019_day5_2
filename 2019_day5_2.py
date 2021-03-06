data = open('./2019_day5_input.txt','r')
array = data.read().split(',')
array = [int(i) for i in array]
#print(array)
#array = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#position in the array
print(len(array))
input = 5
n = 0
output = 0

# if optcode 3,4 = 2 numbers; if 1,2 = 4 numbers
while n < len(array)-1:
    if array[n] == 99:
        print('stop')
        break

    # if 1, add two next positions
    elif int(str(array[n])[-1]) == 1:
        print('1v')
        print(n,'index')
        print(array[n:n+4])
        if array[n] > 999:
            if int(str(array[n])[-3]) == 0:
                array[array[n+3]] = array[array[n+1]]+array[n+2]
            elif int(str(array[n])[-3]) == 1:
                array[array[n+3]] =  array[n+1]+array[n+2]
        elif 999 > array[n] > 99:
            array[array[n+3]] =  array[n+1]+array[array[n+2]]
        elif array[n] < 9:
            array[array[n+3]] = array[array[n+1]]+array[array[n+2]]
        n += 4

    # if 2, multiply two next positions
    elif int(str(array[n])[-1]) == 2:
        print('2v')
        print(n,'index')
        print(array[n:n+4])
        if array[n] > 999:
            if int(str(array[n])[-3]) == 0:
                array[array[n+3]] = array[array[n+1]]*array[n+2]
            elif int(str(array[n])[-3]) == 1:
                array[array[n+3]] = array[n+1]*array[n+2]
        elif 999 > array[n] > 99:
            array[array[n+3]] =  array[n+1]*array[array[n+2]]
        elif array[n] < 9:
            array[array[n+3]] = array[array[n+1]]*array[array[n+2]]
        n += 4

    #if 3, Opcode 3 takes a single integer as input and saves
    #it to the position given by its only parameter
    elif int(str(array[n])[-1]) == 3:
        print("3v")
        print(n,'index')
        print(array[n:n+2])
        if array[n] > 99:
            array[n+1] = input
        else:
            array[array[n+1]] = input
        n += 2

    #if 4, output n+1
    elif int(str(array[n])[-1]) == 4:
        print("4v")
        print(n,'index')
        print(array[n:n+2])
        if array[n] > 99:
            output = array[n+1]
        else:
            output = (array[array[n+1]])
        n += 2

    #if 5: if the first parameter is non-zero,
    #it sets the instruction pointer to the value from the second parameter
    elif int(str(array[n])[-1]) == 5:
        print('5v')
        print(n,'index')
        print(array[n:n+3])
        if array[n] < 9:
            if array[array[n+1]] != 0:
                n = array[array[n+2]]
            else:
                n += 3
        elif array[n] > 999:
            if int(str(array[n])[-3]) == 0:
                if array[array[n+1]] != 0:
                    n = array[n+2]
                else:
                    n += 3
            elif int(str(array[n])[-3]) == 1:
                if array[n+1] != 0:
                    n = array[n+2]
                else:
                    n += 3
        elif 999 > array[n] > 99:
            if array[n+1] != 0:
                n = array[array[n+2]]
            else:
                n += 3

    #if 6, same as 5 just if IS ZERO
    #it sets the instruction pointer to the value from the second parameter.
    elif int(str(array[n])[-1]) == 6:
        print('6v')
        print(n,'index')
        print(array[n:n+3])
        if array[n] < 9:
            if array[array[n+1]] == 0:
                n = array[array[n+2]]
            else:
                n += 3
        elif array[n] > 999:
            if int(str(array[n])[-3]) == 0:
                if array[array[n+1]] == 0:
                    n = array[n+2]
                else:
                    n += 3
            elif int(str(array[n])[-3]) == 1:
                if array[n+1] == 0:
                    n = array[n+2]
                else:
                    n += 3
        elif 999 > array[n] > 99:
            if array[n+1] == 0:
                n = array[array[n+2]]
            else:
                n += 3
    #if 7 if the first parameter is LESS THAN the second parameter,
    #it stores 1 in the position given by the third parameter.
    #Otherwise, it stores 0
    if int(str(array[n])[-1]) == 7:
        print('7v')
        print(n,'index')
        print(array[n:n+4])
        if array[n] > 999:
            if int(str(array[n])[-3]) == 1:
                if array[n+1] < array[n+2]:
                    array[array[n+3]] = 1
                else:
                    array[array[n+3]] = 0
            elif int(str(array[n])[-3]) == 0:
                if array[array[n+1]] < array[n+2]:
                    array[array[n+3]] = 1
                else:
                    array[array[n+3]] = 0
        elif 999 > array[n] > 99:
            if array[n+1] < array[array[n+2]]:
                array[array[n+3]] = 1
            else:
                array[array[n+3]] = 0
        elif array[n] < 9:
            if array[array[n+1]] < array[array[n+2]]:
                array[array[n+3]] = 1
            else:
                array[array[n+3]] = 0
        n += 4

    #if 8 if the first parameter is equal to the second parameter,
    #it stores 1 in the position given by the third parameter.
    #Otherwise, it stores 0
    elif int(str(array[n])[-1]) == 8:
        print('8v')
        print(n,'index')
        print(array[n:n+4])
        if array[n] > 999:
            if int(str(array[n])[-3]) == 1:
                if array[n+1] == array[n+2]:
                    array[array[n+3]] == 1
                else:
                    array[array[n+3]] == 0
            elif int(str(array[n])[-3]) == 0:
                if array[array[n+1]] == array[n+2]:
                    array[array[n+3]] = 1
                else:
                    array[array[n+3]] = 0
        else:
            if array[array[n+1]] == array[array[n+2]]:
                array[array[n+3]]= 1
            else:
                array[array[n+3]] = 0
        n += 4

print(output)
