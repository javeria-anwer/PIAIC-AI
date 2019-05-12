#input 5 subjects marks

math_score = int(input("Please enter Maths's score"))
eng_score = int(input("Please enter English's score"))
physics_score = int(input("Please enter Physics's score"))
chemistry_score = int(input("Please enter Chemistry's score"))
computer_score = int(input("Please enter Computer's score"))

#calculate total marks
total_marks = math_score+eng_score+physics_score+chemistry_score+computer_score

#calculate percentage
percentage = (total_marks / 500)*100

#find out grade

grade = "F"

if(percentage>80):
    grade="A+"
elif(percentage<80 and percentage>=70):
    grade="A"
elif(percentage<70 and percentage >=60):
    grade = "B"
elif(percentage<60 and percentage >=50):
    grade ="C"
else:
    grade = "F"

#print grade
print("You achieved ", grade)

