import psycopg2
import csv

def connect():
    return psycopg2.connect(
        database="task",
        user="postgres",
        password="Aldik2005",
        host="localhost",
        port="5432"
    )

def insert_from_csv(cursor, filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) == 3:
                    name, surname, phone = row
                    cursor.execute(
                        "INSERT INTO PhoneBook (name, surname, phone) VALUES (%s, %s, %s)",
                        (name, surname, phone)
                    )
                else:
                    print(f"Ошибка в строке: {row}")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении CSV. Попробуйте изменить кодировку файла.")
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу.")

def insert_from_input(cursor):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    cursor.execute(
        "INSERT INTO PhoneBook (name, surname, phone) VALUES (%s, %s, %s)",
        (name, surname, phone)
    )

def update_phone(cursor):
    name_to_update = input("Введите имя для обновления телефона: ")
    new_phone = input("Введите новый номер телефона: ")
    cursor.execute(
        "UPDATE PhoneBook SET phone = %s WHERE name = %s",
        (new_phone, name_to_update)
    )

def delete_by_name(cursor):
    name_to_delete = input("Введите имя для удаления: ")
    cursor.execute(
        "DELETE FROM PhoneBook WHERE name = %s",
        (name_to_delete,)
    )

def show_all(cursor):
    cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = connect()
    cursor = conn.cursor()

    try:
        print("1. Загрузить данные из CSV")
        print("2. Ввести данные вручную")
        choice = input("Выберите способ добавления (1/2): ")

        if choice == '1':
            csv_path = input("Введите путь к CSV файлу: ")
            insert_from_csv(cursor, csv_path)
        elif choice == '2':
            insert_from_input(cursor)
        else:
            print("Неверный выбор.")

        print("\nТекущие записи в PhoneBook:")
        show_all(cursor)

        print("\nХотите обновить телефон?")
        if input("Введите 'да' для обновления: ").lower() == 'да':
            update_phone(cursor)
            print("После обновления:")
            show_all(cursor)

        print("\nХотите удалить пользователя?")
        if input("Введите 'да' для удаления: ").lower() == 'да':
            delete_by_name(cursor)
            print("После удаления:")
            show_all(cursor)

    except psycopg2.DatabaseError as e:
        print("Ошибка базы данных:", e)
        conn.rollback()
    finally:
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
