# Данные курсов из лабораторной работы № 3
HOURS = {"Python": 30, "SQL": 24, "Анализ данных": 36}

# Данные курсов из лабораторной работы № 3
HOURS = {
    "Python": 30,
    "SQL": 24,
    "Анализ данных": 36
}

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