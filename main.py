#! /usr/bin/python3

from funcsGradeCal import NumToGPAFunc

gradesGPA = {
        'A':4,
        'B':3,
        'C':2,
        'D':1,
        'F':0,
        'done': 'done'
    }

i = 0
cont = True
num = 0

usrch = input('Would you like to use Letter to GPA(LetToGPA), or Number to GPA (NumToGPA)?\n')

if usrch == 'LetToGPA':

    print("Hello, welcome to the gpa, or grade-point-average calculator. This calculator takes letter grades and turns them into a gpa. If you don't know what a gpa means or converts to it is simple. 4 to 3.1 is an A, 3 to 2.1 is a B, 2 to 1.1 is a D, and a 1 to 0 is an F.")

    while cont != False:
        grd = input('Letter grade: ')

        if grd == 'done':
            cont = False

        elif grd == 'A' or 'B' or 'C' or 'D' or 'F':
            num += gradesGPA[grd]
            i += 1

        else:
            print("Incorrect input, try again.")

    gpa = num / i
    print(f'{gpa:.2f}')

elif usrch == 'NumToGPA':

    print('Hello, welcome to a percent to GPA calculator. Type a negitive number when done.')

    while cont == True:

        grd = int(input("Please input your grade (int only): "))

        if grd <= 100:
            num1 = NumToGPAFunc(grd)

            if num1 == 'done':
                cont = False

            else:
                i += 1
                num += gradesGPA[num1]

        else:
            print('Incorrect Input')
            
    gpa = num / i
    print(f'{gpa:.2f}')