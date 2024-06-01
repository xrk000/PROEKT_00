from tkinter import *
import tkinter as tk

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

menu_canvas.pack()
main_root.mainloop()