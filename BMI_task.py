
def get_bmi(h, w):

    bmi_value = round(w / h ** 2, 2)

    return bmi_value


def get_value(text):

    value = ""
    do_input = True
    while do_input:

        try:
            value = float(input(f"Введите свой {text}: ").replace(",", "."))
            do_input = False
        except ValueError:
            print("Значение должно быть цифрами")

    return value


height_sm = get_value("рост в см")
weight = get_value("вес в кг")


height = round(height_sm / 100, 2)
bmi = get_bmi(height, weight)


print(f"Ваш рост {height}м, ваш вес {weight}кг, ваш ИМТ = {bmi}")


if bmi < 18.5:
    print("Входит в категорию: недостаточная масса тела (меньше 18,5)")
elif 18.5 <= bmi <= 24.9:
    print("Входит в категорию: норма (18,5 - 24,9)")
elif 25 <= bmi <= 29.9:
    print("Входит в категорию: избыточная масса тела (25 - 29,9)")
else:
    print("Входит в категорию: ожирение (30 и выше)")
