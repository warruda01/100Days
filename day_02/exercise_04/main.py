weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.8:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")

print(round(bmi, 2))
print(f"{bmi:.2f}")