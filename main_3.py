# Открываем файл для чтения
file_path = "lessons.txt"

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
    exit()

subject_lessons = {}

for line in lines:
    parts = line.strip().split(':')
    if len(parts) == 2:
        subject_name = parts[0].strip()
        lesson_info = parts[1].strip()

        lesson_numbers = []
        current_number = ""

        for char in lesson_info:
            if char.isdigit():
                current_number += char
            elif current_number:
                lesson_numbers.append(int(current_number))
                current_number = ""

        if current_number:
            lesson_numbers.append(int(current_number))

        total_lessons = sum(lesson_numbers)

        subject_lessons[subject_name] = total_lessons

        total_lessons = 0

print("Общее количество занятий по предметам:")
for subject, total_lessons in subject_lessons.items():
    print(f"{subject}: {total_lessons}")
