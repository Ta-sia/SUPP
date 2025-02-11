import tkinter as tk
import mysql.connector
from mysql.connector import Error

# Функция для подключения к базе данных
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Адрес базы данных (локально для MySQL Workbench)
            database='test_db',  # Название базы данных
            user='root',  # Имя пользователя
            password='your_password'  # Ваш пароль
        )
        if connection.is_connected():
            print("Подключение к базе данных успешно!")
            return connection
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None

# Функция для проверки логина и пароля в базе данных
def check_login():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                       (login_entry.get(), password_entry.get()))
        result = cursor.fetchone()
        if result:
            print("Успешный вход!")
        else:
            print("Неверный логин или пароль!")
        cursor.close()
        connection.close()

# Создание главного окна
window = tk.Tk()
window.title("SUPP")  # Заголовок окна

# Установка размеров окна
window.geometry("400x300")

# Установка минимального размера окна
window.minsize(400, 300)

# Установка фона окна
window.configure(bg="#3A0052")

# Создание фрейма для центрирования
frame = tk.Frame(window, bg="#3A0052")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Поле для ввода логина
login_entry = tk.Entry(frame, fg="gray", bg="#3A0052", font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#8A2BE2")
login_entry.insert(0, "UserName")  # Заполняем placeholder
login_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, login_entry, "UserName"))
login_entry.bind("<FocusOut>", lambda event: restore_placeholder(event, login_entry, "UserName"))
login_entry.grid(row=0, column=0, padx=10, pady=10)

# Поле для ввода пароля
password_entry = tk.Entry(frame, fg="gray", bg="#3A0052", font=("Arial", 12), show="*", bd=2, relief="solid", highlightthickness=2, highlightbackground="#8A2BE2")
password_entry.insert(0, "Password")  # Заполняем placeholder
password_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, password_entry, "Password"))
password_entry.bind("<FocusOut>", lambda event: restore_placeholder(event, password_entry, "Password"))
password_entry.grid(row=1, column=0, padx=10, pady=10)

# Кнопка ВОЙТИ
def on_hover(event):
    login_button.config(bg="#8A2BE2", fg="black", relief="flat")

def on_leave(event):
    login_button.config(bg="#3A0052", fg="#8A2BE2", relief="solid")

login_button = tk.Button(frame, text="Play", bg="#3A0052", fg="#8A2BE2", font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="#8A2BE2", command=check_login)
login_button.grid(row=2, columnspan=2, pady=20)

# Настройка событий наведения для кнопки
login_button.bind("<Enter>", on_hover)
login_button.bind("<Leave>", on_leave)

# Запуск основного цикла приложения
window.mainloop()
