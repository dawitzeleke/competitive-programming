def gradingStudents(grades):
    res=[]
    for grade in grades:
        if grade>=38:
            mod5= grade%5
            rounded= 5-mod5
            if (rounded)<3:
                grade= (grade-mod5)+5
        res.append(grade)
    return res
