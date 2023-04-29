usrch = input('Would you like to use Letter to GPA(LetToGPA), or Number to Letter grade average(NumToLet)?')

if usrch == 'LetToGPA':
    fin = 0
    i = 0
    cont = True
    num = 0

    gradesGPA = {
        'A':4,
        'B':3,
        'C':2,
        'D':1,
        'F':0,
    }
    gradesLetNum = {
        100 <= 90: 'A',
        89 <= 80: 'B',
        79 <= 70: 'C',
        69 <= 60: 'D',
        59 <= 0: 'F',
    }

    print("Hello, welcome to the gpa, or grade-point-average calculator. This calculator takes letter grades and turns them into a gpa. If you don't know what a gpa means or converts to it is simple. 4 to 3.1 is an A, 3 to 2.1 is a B, 2 to 1.1 is a D, and a 1 to 0 is an F.")

    while cont != False:
        grd = input('Grade: ')
    
        if grd == 'done':
            cont = False
        elif grd == 'A' or 'B' or 'C' or 'D' or 'F':
            num += gradesGPA[grd]
            i += 1
            num += fin
        else:
            print("Incorrect input, try again.")

    gpa = num / i

    print(f'{gpa:.2f}')
elif usrch == 'NumToLet':
    print('Hello, welcome to a letter(s) to letter grade average calculator. Type "done" when done.')
    while cont != False:
        grd = int(input("Please input your grade (int only): "))
        if grd == 