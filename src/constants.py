import enum


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
