def is_glsn(char):
    glsn = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return char in glsn
def is_sogl(char):
    sogl = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    return char in sogl
user_input = input("Введите строку на русском языке: ")
glsn_count = 0
sogl_count = 0
for char in user_input:
    if is_glsn(char):
        glsn_count += 1
    elif is_sogl(char):
        sogl_count += 1
print(f"Длина строки: {len(user_input)}")
print(f"Количество гласных: {glsn_count}")
print(f"Количество согласных: {sogl_count}")
