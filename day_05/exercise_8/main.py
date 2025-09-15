student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
sum = 0
high = 0
low = 10000
for n in student_scores:
    sum += n
    if n > high:
        high = n
    if n < low:
        low = n

print(sum)
print(low)
print(high)