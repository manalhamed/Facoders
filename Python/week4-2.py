print('Number from 1 to 10')
x=5
num = int(input('Guess the number: '))
while num != x and num <=10 and num >=1:
    num =int(input('Guess the number: '))
    if num==x:
        print('Great! You did it!')
