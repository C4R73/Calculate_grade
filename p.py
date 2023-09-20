def calculate_grade(assignment1, assignment2, finalexam, participation):
    grade1= assignment1 * 0.25
    grade2 = assignment2 * 0.25
    part = participation * 0.10
    final = finalexam * 0.40
    gradeend = grade1 + grade2 + final + part
    return gradeend

print("Final grade")
#I use it to calculate my grades at school :D
g1 = float(input("Please add the grade of your first assignment: "))
g2 = float(input("Please add the grade of your second assignment: "))
part = float(input("Please add the grade of your participation activity: "))
fin = float(input("Please add the grade of your final exam: "))

final_final = calculate_grade(g1, g2, part, fin)
print(int(final_final))
print()
