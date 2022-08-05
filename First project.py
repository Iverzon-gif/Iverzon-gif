# Weighted Exam Score Averange

# Enteing how many exams you have done
number_of_exam = int(input("Enter number of exam:"))

# Entering how many cresits these exam cover
total_credits = int(input("Enter how many credits these exam cover: "))

# Begin with average of 0 and then add uo percentages from each exam
average = 0
for exam in range(number_of_exam):
    score = int(input("Enter exam score"))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)