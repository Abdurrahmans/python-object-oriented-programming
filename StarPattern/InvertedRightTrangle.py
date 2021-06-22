number = int(input("Enter the number of rows: "))
for i in range(0,number):
    for j in range(i, number):
        print('* ',end=' ')
    print('\r')


