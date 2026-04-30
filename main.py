# Grading System (Trial)

name = input("Enter name: ")
exam_score = int(input("Exam score: "))
assessment_score = int(input("Assessment score: "))
fees_paid = int(input("Fees paid: "))

total_score = exam_score + assessment_score

print("\nResults for", name)

# Exam verification
if exam_score >= 25:
    print("Exam: Pass")
else:
    print("Exam: Fail")

# Assessment verification
if assessment_score >= 15:
    print("Assessment: Pass")
else:
    print("Assessment: Fail")

# Main decision logic
if exam_score >= 25 and assessment_score >= 15:
    if fees_paid == 100:
        print("Status: Certificate issued")
    else:
        print("Status: Passed, but fees incomplete")

elif total_score == 39:
    print("Status: Condoned")
    if fees_paid == 100:
        print("Status: Certificate issued")
    else:
        print("Status: Please pay fees for certificate")

else:
    print("Status: Fail")

# Retake condition
if exam_score < 25 and assessment_score < 15:
    print("Recommendation: Repeat both components")