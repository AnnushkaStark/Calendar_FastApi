import enum

MIN_LENGTH_TITLE = 3
MAX_LENGTH_TITLE = 3
MAX_LENGTH_DESRIPTION = 1500


class EventType(enum.StrEnum):
    """
    Тип события:
    - Встреча
    - Задача
    - Важная дата
    - Личное
    - Без категории
    (дефолное)
    """
    meeting = "meeting"
    task = "task"
    important_date = "important date"
    personal = "personal"
    no_category = "no category"


class EventPriority(enum.StrEnum):
    """
    Приоретет события
    -важное 
    -требует  внимания
    -без приоритета
    (дефолтное)
    """
    important = "important"
    requires_attention = "requires attention"
    without_priority = "without priority"


class EventLocation(enum.StrEnum):
    """
    Место проведения события
    - Skype
    - Zoom
    - GogleMeet
    - Telegram
    - Б24
    - Другое (дефолтное)
    """
    skype = "skype"
    zoom = "zoom"
    goglemeet = "GoogleMeet"
    telegram = "Telegram"
    b24 ="B24"
    other = "Другое"

# Пока не реализовано
class EventRepitabilyty(enum.StrEnum):
    """
    Повторяемость события
    - каждый день
    - каждую неделю
    - каждый месяц
    - без повторов
    (дефолтное)
    """
    every_day ="every day"
    every_week = "every week"
    every_month = "every month"
    no_repeats =  "no repeats"

