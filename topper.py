total_students= int(input("Enter total no of students"))
#read student marks
tel_marks=[]
hin_marks=[]
eng_marks=[]
math_marks=[]
science_marks=[]
social_marks=[]
total_marks=[]
student_names=[]

for i in range(total_students):
    student_names=list(map(str,input().split()))
    tel_marks,hin_marks,eng_marks,math_marks,science_marks,social_marks=map(int,input("Enter marks: "))
    total_marks=list(tel_marks+hin_marks+eng_marks+math_marks+science_marks+social_marks)
    total_marks.append(total_marks)
    topper_ind=[] 