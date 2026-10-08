
import telebot
from config import TOKEN
from functions import get_courses, course_info, total_hours, format_user, get_contacts, get_tips, courses_list, calculate_average, sort_students_asc, sort_students_desc
from validators import check_email, extract_numbers, check_phone

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте!\n"
        "Я учебный бот.\n\n"
        "Доступные команды:\n"
        "/courses — список курсов\n"
        "/contacts — контакты\n"
        "/stats — статистика пользователей\n"
        "/hours — длительность курсов\n"
        "/schedule — расписание\n"
        "/countdown — обратный отсчёт\n"
        "/tip — полезный совет\n"
        "/info Python — информация о курсе\n"
        "/me — информация о пользователе\n"
        "/email — проверка email\n"
        "/average — посчитать среднее\n"
        "/phone — проверка номера\n"
        "/sort_asc — сортировка студентов по возрастанию\n"
        "/sort_desc — сортировка студентов по убыванию\n"
        "/numbers — поиск чисел"
    )


@bot.message_handler(commands=["sort_asc"])
def sort_asc(message):
    students = sort_students_asc()
    text = "Студенты по возрастанию балла:\n"
    for student in students:
        text += f"{student['name']} — {student['score']}\n"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["sort_desc"])
def sort_desc(message):
    students = sort_students_desc()
    text = "Студенты по убыванию балла:\n"
    for student in students:
        text += f"{student['name']} — {student['score']}\n"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["phone"])
def phone(message):
    try:
        phone_number = message.text.split(maxsplit=1)[1].strip()
        if check_phone(phone_number):
            result = "Номер телефона корректный."
        else:
            result = "Некорректный номер телефона."
    except IndexError:
        result = "Используйте команду:\n/phone +77001234567"

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["average"])
def average(message):
    try:
        parts = message.text.split()[1:]
        numbers = [float(number) for number in parts]
        result = calculate_average(*numbers)
        bot.send_message(
            message.chat.id,
            f"Среднее значение: {result}"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            "Ошибка: вводите только числа."
        )

@bot.message_handler(commands=["courses"])
def show_courses(message):
    data = courses_list()
    text = "Курсы:\n" + "\n".join(data)
    text += f"\nВсего: {len(data)}, первый: {data[0]}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["contacts"])
def show_contacts(message):
    center, phone = get_contacts()
    bot.send_message(message.chat.id, f"{center}\nТелефон: {phone}")

@bot.message_handler(commands=["courses"])
def courses(message):
    data = get_courses()
    # Сортировка курсов по количеству часов с помощью lambda
    sorted_courses = sorted(data.items(), key=lambda item: item[1])
    lines = ["Доступные курсы:"]
    for name, hours in sorted_courses:
        lines.append(f"{name} — {hours} ч.")
    # Распаковка значений словаря в функцию с *args
    lines.append(f"Всего: {total_hours(*data.values())} ч.")
    bot.send_message(message.chat.id, "\n".join(lines))

@bot.message_handler(commands=["info"])
def info(message):
    try:
        name = message.text.split(maxsplit=1)[1]
        result = course_info(name)
    except IndexError:
        result = "Используйте команду:\n/info Python"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["me"])
def me(message):
    user = message.from_user
    # Передача именованных аргументов в функцию с **kwargs
    result = format_user(
        Имя=user.first_name,
        Username=user.username,
        ID=user.id
    )
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["email"])
def email(message):
    try:
        email = message.text.split(maxsplit=1)[1]
        if check_email(email):
            result = "Email корректный."
        else:
            result = "Некорректный email."
    except IndexError:
        result = "Используйте команду:\n/email student@example.com"
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["numbers"])
def numbers(message):
    text = message.text
    numbers = extract_numbers(text)
    if numbers:
        result = "Найденные числа: " + ", ".join(numbers)
    else:
        result = "Числа не найдены."
    bot.send_message(message.chat.id, result)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    try:
        numbers = extract_numbers(message.text)
        if numbers:
            bot.send_message(
                message.chat.id,
                f"Я нашёл числа: {', '.join(numbers)}"
            )
        else:
            bot.send_message(
                message.chat.id,
                "Сообщение получено. Используйте /start."
            )
    except Exception as error:
        print("Ошибка:", error)
        bot.send_message(
            message.chat.id,
            "Произошла ошибка при обработке сообщения."
        )


bot.infinity_polling()