#Fayldan o‘qish
with open("data.txt", "r") as f:
    lines = f.readlines()

students = []

# O‘qish va tekshirish
for line in lines:
    name, grade = line.strip().split(",")
    if grade.isdigit():
        grade = int(grade)
        if 2 <= grade <= 5:  # faqat 2-5 oralig‘i
            students.append((name, grade))

# Yangi talaba qo‘shish
name = input("Ism kiriting: ")
grade = input("Baho kiriting (2-5): ")

if grade.isdigit():
    grade = int(grade)
    if 2 <= grade <= 5:
        with open("data.txt", "a") as f:
            f.write(f"{name},{grade}\n")

# Statistik hisoblash
grades = [s[1] for s in students]

if grades:
    avg = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)

# Saralash
students.sort(key=lambda x: x[1], reverse=True)

# Natijani yozish
with open("result.txt", "w") as f:
    f.write("Talabalar:\n")
    for s in students:
        f.write(f"{s[0]} - {s[1]}\n")

    f.write("\nStatistika:\n")
    f.write(f"O‘rtacha baho: {avg:.2f}\n")
    f.write(f"Eng yuqori: {max_grade}\n")
    f.write(f"Eng past: {min_grade}\n")

# Qidiruv
search = input("Qidirish uchun ism: ")
for s in students:
    if search.lower() in s[0].lower():
        print("Topildi:", s)
