grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

teach= input("Choose one: students_names, student_score, students_count")
if teach == 'students_names':
    grade= input('Enter grade: ')
    def students_names(grade):
        a=list(grade.keys())
        return a
        if grade =="grade_one":
            print(students_names(grade_one))
        elif grade =="grade_two":
            print(students_names(grade_two))
        elif grade =="grade_three":
            print(students_names(grade_three))

elif teach == 'student_score':
    grade,name =input('Enter grade: '), input('Enter name: ')
    def student_score(grade,name):
        m =sum(grade.get(name))
        return m
    if grade =="grade_one":
        for i in students_names(grade_one):
            if name == i:
                print(student_score(grade_one,i))
    elif grade =="grade_two":
        for i in students_names(grade_two):
            if name == i:
                print(student_score(grade_two,i))
    elif grade =="grade_three":
        for i in students_names(grade_three):
            if name == i:
                print(student_score(grade_three,i))

elif teach == 'students_count':
    grade = input('Enter grade: ')
    def students_count(grade):
        a =len(list(grade.keys()))
        return a
    if grade =="grade_one":
        print(students_count(grade_one))
    elif grade =="grade_two":
        print(students_count(grade_two))
    elif grade =="grade_three":
        print(students_count(grade_three))
x = input('done or more: ')
if x=='done':
    exit
elif x=='more':
    teach= input ("Choose one: students_names, student_score, students_count")
