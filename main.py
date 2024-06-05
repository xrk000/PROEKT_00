from tkinter import *
import tkinter as tk
from quiz_data import quiz_data
import random
from tkinter import messagebox, ttk

def clear_content1():
    # Удаление всех виджетов на главном экране
    for widget in menu_canvas.winfo_children():
        widget.destroy()

def clear_and_show_new_content2():
    clear_content1()
    show_new_content2()

def show_new_content2():
    def show_question():
        # Получите текущий вопрос из списка quiz_data
        global list_of_questions
        if len(list_of_questions) == 0:

            list_of_questions = quiz_data
            random.shuffle(list_of_questions)

        question = list_of_questions[current_question]
        qs_label.config(text=question["question"])

        # Отображение выбора на кнопках
        choices = question["choices"]
        random.shuffle(choices)
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

        # Очистите метку отзыва и отключите кнопку «Далее»
        feedback_label.config(text="")
        next_btn.config(state="disabled")

    # Функция проверки выбранного ответа и отзыва
    def check_answer(choice):
        # Получите текущий вопрос из списка quiz_data
        question = list_of_questions[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Проверьте, соответствует ли выбранный вариант правильному ответу
        if selected_choice == question["answer"]:
            # Обновите счет и отобразите его
            global score
            score += 1
            score_label.config(text="Результат: {}/{}".format(score, len(quiz_data)))
            feedback_label.config(text="Правильно!", foreground="green")
        else:
            selected_theme = quiz_data[current_question]["Theme"]
            global count_of_wrong_answers
            value = count_of_wrong_answers[selected_theme]
            value += 1
            count_of_wrong_answers[selected_theme] = value
            print(count_of_wrong_answers)
            feedback_label.config(text="Не правильно!", foreground="red")

        # Отключить все кнопки выбора и включить кнопку «Далее»
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Функция перехода к следующему вопросу
    def next_question():
        global count_of_wrong_answers, current_question, questions_by_theme, score, list_of_questions

        current_question += 1
        if current_question < len(list_of_questions):
            # Если есть еще вопросы, покажите следующий вопрос
            show_question()
        else:
            # Если на все вопросы даны ответы, отобразите окончательный результат и завершите тест.
            recomen = "Вам следует повторить: "
            for key in count_of_wrong_answers:
                count = count_of_wrong_answers[key]
                if count > 1:
                    recomen = recomen + key + "; "
                    count_of_wrong_answers[key] = recomen
                else:
                    continue
            if recomen == "Вам следует повторить: ":
                recomen = ""

            messagebox.showinfo("Тест завершён!",
                                ("Тест завершён! Ваш результат: {}/{}").format(score, len(quiz_data)) + "\n{}".format(recomen))

            score = 0
            count_of_wrong_answers = {"Географические особенности природы материков и океанов, народов Земли": 0,
                                      "Политико-административное положение России": 0,
                                      "Особенности природы России": 0}

            questions_by_theme = []
            list_of_questions = []
            # Инициализировать текущий указатель вопросов
            current_question = 0
            clear_and_show_old_content()

    # Создайте метку вопроса
    qs_label = Label(
        menu_canvas,
        anchor="center",
        width=43,
        wraplength=500,
        font=("Georgia", 20),
        foreground="white",
        background="green"
    )
    qs_label.place(x=2, y=75)

    # Создайте кнопки выбора
    choice_btns = []
    y = 175
    for n in range(4):

        button = Button(
            menu_canvas,
            command=lambda i=n: check_answer(i),
            height=2,
            width=40,
            fg="white",
            bg="green",
            activebackground="#07d933",
            activeforeground="#fff",
            font=("Georgia", 13)
        )
        button.place(x=145, y=y)
        y += 60
        choice_btns.append(button)

    # Создайте ярлык отзыва
    feedback_label = Label(
        menu_canvas,
        font=("Georgia", 13),
        anchor="center",
        foreground="white",
        background="lime",
        padx=10,
        pady=5,
        height=2,
        width=12
    )
    feedback_label.place(x=410, y=425)

    # Создайте метку оценки
    score_label = Label(
        menu_canvas,
        font=("Georgia", 13),
        text="Score: 0/{}".format(len(quiz_data)),
        foreground="white",
        background="green",
        padx=10,
        pady=5,
        height=2
    )
    score_label.place(x=145, y=425)

    # Создать следующую кнопку
    next_btn = Button(
        menu_canvas,
        text="Следующий вопрос >>>",
        command=next_question,
        state="disabled",
        width=27,
        height=2,
        fg="white",
        bg="green",
        activebackground="#07d933",
        activeforeground="#fff"
    )
    next_btn.place(x=355, y=500)

    end_btn = Button(
        menu_canvas,
        command=clear_and_show_old_content,
        text="Главное меню",
        width=27,
        height=2,
        fg="white",
        bg="green",
        activebackground="#07d933",
        activeforeground="#fff"
    )
    end_btn.place(x=145, y=500)

    # Покажи первый вопрос
    show_question()

def clear_and_show_old_content():
    global count_of_wrong_answers, current_question_by_theme, score, current_question, questions_by_theme, list_of_questions
    score = 0
    list_of_questions = []
    count_of_wrong_answers = {"Географические особенности природы материков и океанов, народов Земли": 0,
                              "Политико-административное положение России": 0,
                              "Особенности природы России": 0}

    questions_by_theme = []
    # Инициализировать текущий указатель вопросов
    current_question = 0
    current_question_by_theme = 0
    clear_content1()
    # Отображение старого содержимого
    btn1 = tk.Button(menu_canvas,
                     text="Начать тест",
                     command=clear_and_show_new_content2,
                     activebackground="#07d933",
                     activeforeground="#fff",
                     font=("Georgia", 16),
                     width="27",
                     height="2",
                     fg="white",
                     bg="green")
    btn1.place(x=180, y=200)

    btn2 = tk.Button(menu_canvas,
                     text="Тест по темам",
                     activebackground="#07d933",
                     activeforeground="#fff",
                     font=("Georgia", 16),
                     width="27",
                     height="2",
                     fg="white",
                     bg="green")
    btn2.place(x=180, y=275)

    btn3 = tk.Button(menu_canvas,
                     text="Выход",
                     command=main_root.quit,
                     activebackground="#07d933",
                     activeforeground="#fff",
                     font=("Georgia", 16),
                     width="27",
                     height="2",
                     fg="white",
                     bg="green")
    btn3.place(x=180, y=350)

    label1 = Label(menu_canvas,
                   text="                                                            Поддержка:nik.ars06@bk.ru                                                            ",
                   font=("Georgia", 12),
                   fg="white",
                   bg="green")
    label1.place(x=2, y=574)

    label2 = Label(menu_canvas,
                   text="         Тест по географии и биологии для проверки        \n знаний школьного курса",
                   font=("Georgia", 20),
                   fg="white",
                   bg="green")
    label2.place(x=2, y=60)

main_root = Tk()
# main_root.config(cursor='man')
main_root.title("Тест")
main_root.geometry("700x600")
main_root.resizable(width=False, height=False)

menu_canvas = Canvas(main_root,
                     width=700,
                     height=600)
image = tk.PhotoImage(file="azx.png")
menu_canvas.create_image(0, 0, image=image, anchor="nw")

btn1 = tk.Button(menu_canvas,
                 text="Начать тест",
                 command=clear_and_show_new_content2,
                 activebackground="#07d933",
                 activeforeground="#fff",
                 font=("Georgia", 16),
                 width="27",
                 height="2",
                 fg="white",
                 bg="green")
btn1.place(x=180, y=200)

btn2 = tk.Button(menu_canvas,
                 text="Тест по темам",
                 activebackground="#07d933",
                 activeforeground="#fff",
                 font=("Georgia", 16),
                 width="27",
                 height="2",
                 fg="white",
                 bg="green")
btn2.place(x=180, y=275)

btn3 = tk.Button(menu_canvas,
                 text="Выход",
                 command=main_root.quit,
                 activebackground="#07d933",
                 activeforeground="#fff",
                 font=("Georgia", 16),
                 width="27",
                 height="2",
                 fg="white",
                 bg="green")
btn3.place(x=180, y=350)

label1 = Label(menu_canvas,
               text="                                                        Тех.поддержка:nik.ars06@bk.ru                                                            ",
               font=("Georgia", 12),
               fg="white",
               bg="green")
label1.place(x=2, y=574)

label2 = Label(menu_canvas, text="         Тест по географии и биологии для проверки        \n знаний школьного курса",
               font=("Georgia", 20),
               fg="white",
               bg="green")
label2.place(x=2, y=60)

# Инициализировать рекорд
score = 0
count_of_wrong_answers = {"Географические особенности природы материков и океанов, народов Земли": 0,
                          "Политико-административное положение России": 0,
                          "Особенности природы России": 0}

questions_by_theme = []
list_of_questions = []
# Инициализировать текущий указатель вопросов
current_question = 0
current_question_by_theme = 0

menu_canvas.pack()
main_root.mainloop()