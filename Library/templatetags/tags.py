# custom_tags.py
from django import template

register = template.Library()

@register.simple_tag
def get_lesson_time(lesson_number):
    lesson_times = {
        1: ("8:30", "09:50"),
        2: ("10:00", "11:20"),
        3: ("11:40", "13:00"),
        4: ("13:30", "14:50"),
        5: ("15:00", "16:20"),
        6: ("16:30", "17:50")
    }
    start_time, end_time = lesson_times.get(lesson_number, ("", ""))
    return f"{start_time} - {end_time}"