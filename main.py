from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from random import shuffle, choice
from time import sleep

app = QApplication([])
from main_window import *
from menu_window import*

# Клас для створення запитань
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attempt = 0
    
    # метод для врахування неправильної відповіді
    def got_wrong(self):
        self.attempt += 1
    
    # метод для врахування правильної відповіді
    def got_right(self):
        self.attempt += 1
        self.correct += 1

# створюємо 4 питання (об'єкти класу Question)
q1 = Question("Яблуко", "apple", "application", "apply", "pinapple")
q2 = Question("Дім", "house", "horse", "hurry", "hour")
q3 = Question("Миша", "mouse", "tiger", "mouth", "museum")
q4 = Question("Число", "number", "digit", "amount", "summary")


# список кнопок та список питань
questions = [q1, q2, q3, q4] 
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 

# Функція, яка вдіображає нове питання та варіанти відповідей до нього
def new_question():
    # обираємо рандомне питання
    global current_question
    current_question = choice(questions) 
    # розставляємо по віджетам формулюваня питання та його правильну відповідь
    lb_Question.setText(current_question.question)
    lb_Correct.setText(current_question.answer)
    # перемішуємо радіокнопки
    shuffle(radio_buttons)
    # розставляємо варіанти відповідей
    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)

new_question()


# Функція, яка перевіряє обрану відповідь
def check():
    for button in radio_buttons:
        if button.isChecked():
            if button.text() == lb_Correct.text():
                lb_Result.setText("Правильно")
                current_question.got_right()
            else:
                lb_Result.setText("Неправильно")
                current_question.got_wrong()



# Функція, яка буде спрацьовувати при натисканні на кнопку "Відповісти"
def click_ok():
    if btn_OK.text() == "Відповісти":
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText("Наступне питання")
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText("Відповісти")

# підключаємо функцію click_ok() до кнопки "Відповісти"
btn_OK.clicked.connect(click_ok)


# Функція, яка запускає "Відпочинок"
def rest():
    window.hide()
    minites = box_Minutes.value() * 60
    sleep(minites)
    window.show()

# підключаємо функцію rest() до кнопки "Відпочити"
btn_Sleep.clicked.connect(rest)


# функція, яка відкриває Меню та ховає головне вікно
def open_menu():
    window.hide()
    menu_window.show()

# підключаємо функцію open_menu() до кнопки "Меню"
btn_Menu.clicked.connect(open_menu)


# функція, яка відкриває головне вікно та ховає меню
def back():
    menu_window.hide()
    window.show()

# підключаємо функцію back() до кнопки "Назад"
btn_back.clicked.connect(back)


# функція, яка додає нове питання до списку запитань
def add_question():
    new_question_text = le_question.text()
    new_right_answer = le_right_answer.text()
    new_wrong_answer1 = le_wrong_answer1.text()
    new_wrong_answer2 = le_wrong_answer2.text()
    new_wrong_answer3 = le_wrong_answer3.text()
    new_question = Question(new_question_text, new_right_answer, new_wrong_answer1, new_wrong_answer2, new_wrong_answer3)
    questions.append(new_question)
# підключаємо функцію add_question() до кнопки "Додати питання"
btn_add_question.clicked.connect(add_question)


# функція, яка очищає значення всіх QLineEdit
def clear():
    le_question.clear()
    le_right_answer.clear()
    le_wrong_answer1.clear()
    le_wrong_answer2.clear()
    le_wrong_answer3.clear()
# підключаємо функцію clear() до кнопки "Очистити"
btn_clear.clicked.connect(clear)

window.show()
app.exec()