# Read two scores from the user
score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))

distance1 = 10.0 - score1
distance2 = 10.0 - score2

average_score = (score1 + score2) / 2

distance_average = 10.0 - average_score

if average_score >= 6.0:
    status = "Passed"
else:
    status = "Failed"

print(f"Distance of first score from 10: {distance1:.2f}")
print(f"Distance of second score from 10: {distance2:.2f}")
print(f"Average score: {average_score:.2f}")
print(f"Distance of average score from 10: {distance_average:.2f}")
print(f"Status: {status}")
