from telebot import types
from ..api.db import GlobalDb

db = GlobalDb()


def get_markup_classes():
    markup_classes = types.InlineKeyboardMarkup(row_width=2)
    classes = db.get_all_classes()

    for i in classes:
        temp_markup = types.InlineKeyboardButton(text=str(i), callback_data=f'')
        markup_classes.add(temp_markup)

    return markup_classes

def get_markup_subjects(d_class):
    markup_subjects = types.InlineKeyboardMarkup(row_width=2)
    subjects = db.get_all_subjects(d_class)

    for i in subjects:
        temp_markup =



