grade = int(input("Enter the student's grade: "))
if grade == 100:
    print("Excellent, you passed with flying colors!")
elif 90 <= grade < 100:
    print("You got great marks!")
elif 80 <= grade < 90:
    print("You got good marks!")
elif 70 <= grade < 80:
    print("You got decent marks!")
elif 60 <= grade < 70:
    print("You passed, but there's room for improvement.")
elif 50 <= grade < 60:
    print("You just passed, but need to work harder next time.")
else:
    print("You failed. Better luck next time!")
        
