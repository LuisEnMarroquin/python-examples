studentGrade = input("Enter student's grade: ")

def evaluate(grade):
  value = 'approved'
  if grade < 70:
    value = 'disapproved'
  return value

print(evaluate(int(studentGrade)))
