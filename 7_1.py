# سوال : تو چقدر اضافه وزن داری؟
weight = int(input())
height = float(input())

BMI = weight/(height * height)
print(f"{BMI:.2f}")

if BMI < 18.5:
    print("Underweight")
if 18.5 <= BMI < 25:
    print("Normal")
if 25 <= BMI < 30:
    print("Overweight")
if 30 <= BMI:
    print("Obese")