
# Данные курсов из лабораторной работы № 3
HOURS = {
    "Python": 30,
    "SQL": 24,
    "Анализ данных": 36
}
courses = ["Python", "SQL", "Анализ данных"]
CONTACTS = ("Учебный центр", "+7 700 000 00 00")
users = set()
SCHEDULE = {
    "Понедельник": ["Python", "SQL"],
    "Среда": ["Анализ данных"],
}
TIPS = (
    "Индексы начинаются с 0.",
    "Кортеж нельзя изменить.",
    "while работает, пока условие истинно."
)
PRICES = {
    "Python": 50000,
    "SQL": 40000,
    "Анализ данных": 60000
}
students = [
    {"name": "Анна", "score": 85},
    {"name": "Иван", "score": 72},
    {"name": "Олег", "score": 95}
]

def sort_students_asc():
    return sorted(students, key=lambda student: student["score"])
def sort_students_desc():
    return sorted(students, key=lambda student: student["score"], reverse=True)

def create_student(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f"{key}: {value}")
    return "\n".join(result)

def calculate_average(*numbers):
    if not numbers:
        return "Числа не переданы."
    return sum(numbers) / len(numbers)

def get_course_price(name):
    price = PRICES.get(name)
    if price is None:
        return "Такого курса нет."
    return f"Стоимость курса {name}: {price} тг."

def courses_list():
    return courses

def get_contacts():
    name, phone = CONTACTS
    return (
        f"Название: {name}\n"
        f"Телефон: {phone}"
    )

def get_tips():
    return TIPS

def get_courses():
    return HOURS

def course_info(name):
    hours = HOURS.get(name)
    if hours is None:
        return "Такого курса нет."
    return f"Курс: {name}\nПродолжительность: {hours} ч."

def total_hours(*hours):
    return sum(hours)

def format_user(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f"{key}: {value}")
    return "\n".join(result)

