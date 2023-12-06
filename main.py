import os
import json

try:
    file_path1 = "f1.txt"
    file_path2 = "f2.txt"

    with open(file_path1, "w") as file1:
        print(f"Файл {file_path1} был создан")
        while True:
            line = input("Введите строку (или нажмите Enter для завершения ввода)")
            if not line:
                break
            file1.write(line + "\n")
        print("Данные были успешно записаны в файл!")

    digit_count = 0

    with open(file_path1, "r") as file1, open(file_path2, "w") as file2:
        for line in file1:
            line_words = line.split()
            if line_words[0] == line_words[1]:
                file2.write(line)

    with open(file_path2, "r") as file2:
        last_line = None
        for line in file2:
            last_line = line
        line_words = last_line.split()
        for word in line_words:
            for char in word:
                if char.isdigit():
                    digit_count += 1

    with open("f2.txt", "r") as file2:
        print(f"Данные, скопированнные из {file_path2}: ")
        for line in file2:
            print(line)
    print(f"Количество цифр в последней строке файла F2: {digit_count}")


except IOError:
    print("Произошла ошибка ввода-вывода!")
