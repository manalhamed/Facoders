student= input("Enter student's name: ")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

if student==s1[0]:
    print(s1[0] ,sum(s1[1:6]))
elif student==s2[0]:
    print(s2[0] ,sum(s2[1:6]))
elif student==s3[0]:
    print(s3[0] ,sum(s3[1:6]))
else:
    print('Student is not recorded 0')
