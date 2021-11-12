prelims = int(input('Enter Prelims Grade:'))
midterms = int(input('Enter Midterm Grade:'))
semifinals = int(input('Enter Semi-Finals Grade:'))
finals = int(input('Enter Finals Grade:'))

average = (prelims + midterms + semifinals + finals)/4


if (average < 60):
    print("Your grade is E")
elif(average >= 61 or average <= 70):
    print("Your grade is E")
elif(average >= 71 or average <= 79):
    print("Your grade is D")
elif(average >= 80 or average <= 89):
    print("Your grade is C")
elif(average >= 90 or average <= 98):
    print("Your grade is B")
elif(average > 99):
    print("Your grade is A")