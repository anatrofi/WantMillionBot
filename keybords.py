from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

startbut = InlineKeyboardButton('Начнём!', callback_data='first')
helptbut = InlineKeyboardButton('Что за викторина?', callback_data='help')
sbut = InlineKeyboardMarkup().add(startbut, helptbut)

y_but = InlineKeyboardButton('Новая игра', callback_data='first')
y_but = InlineKeyboardButton('Новая игра', callback_data='first')
choice = InlineKeyboardMarkup().add(y_but)

rest = InlineKeyboardButton('Новая игра', callback_data='first')
restart = InlineKeyboardMarkup().add(rest)

letsstart_but = InlineKeyboardButton('Играть', callback_data='first')
letsstart = InlineKeyboardMarkup().add(letsstart_but)

BUTTONS ={
    'start': sbut,
    'choose': choice,
    'again': restart,
    'letsgo': letsstart
}
