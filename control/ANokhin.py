1)б
2)в
3)а
4)в
5)б
6)б
7)а
8)а
9)
10)в

11.
ошибка 1: вторым аргументом в cursor.execute передана строка title вместо кортежа. Из-за этого SQLite начнет разбивать строку посимвольно

как исправить: передать кортеж с одним элементом: (title,)


ошибка 2: отсутствует вызов conn.commit() Изменения останутся в памяти и не запишутся на диск

как исправить: добавить строку conn.commit() перед возвратом значения


ошибка 3: соединение с базой данных conn не закрывается. Это приводит к утечке ресурсов и блокировкам файла БД

как исправить: добавить закрытие соединения conn.close()

Задание 12

python
import sqlite3

def delete_task_by_id(task_id):
    conn = None
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        return deleted_rows
    except sqlite3.Error:
        if conn:
            conn.rollback()
        return 0
    finally:
        if conn:
            conn.close()

Задание 13. Мини-сценарий

1. Браузер перехватывает отправку формы и отправляет HTTP-запрос методом POST на адрес
2. Маршрут Flask принимает POST-запрос и извлекает текст задачи из request.form.get('title')
3. Flask-приложение открывает соединение с БД командой sqlite3.connect('app.db')
4. Вызывается безопасный параметризованный метод cursor.execute("INSERT INTO tasks ...", (title,))
5. При успешном выполнении вызывается conn.commit() для сохранения записи (или conn.rollback() при ошибке)
6. Блок finally гарантированно закрывает подключение с помощью conn.close()
7. Сервер отправляет браузеру редирект redirect(url_for('index')), давая команду сделать GET-запрос
8. Браузер загружает главную страницу заново (GET), и пользователь видит обновленный список с новой задачей
