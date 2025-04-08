student_marks=int(input("enter marks"))

if student_marks > 50:
    print("scored 50 marks")
    if student_marks>60:
        print("scored 60")
        if student_marks>70:
            print("scored 70 marks")

        else:
            print("not scored above 70")
else:
    print("fail")