import json 
import sqlite3

conn = sqlite3.connect("Base_Books.db")
cursor = conn.cursor()


def add_book():
    name = input("name: ")
    author_name = input("author: ")
    ganre = input("ganre: ")
    year = input("year: ")

    cursor.execute("SELECT author_id FROM authors_table WHERE name = ? ", (author_name,))
    author_row = cursor.fetchone()
    author_id = author_row[0]


    cursor.execute("""
                   INSERT INTO books_table (name, author_id, ganre, years) VALUES (?, ?, ?,?)
                   """,
                    (name, author_id, ganre, year))
    conn.commit()


#выбрать
def get_book():
    book_name = input("search: ")

    cursor.execute("""SELECT books_table.book_id, authors_table.name, books_table.name FROM authors_table
                INNER JOIN books_table ON authors_table.author_id = books_table.author_id 
                WHERE books_table.name = ?
                   """,
                   (book_name,))
    book = cursor.fetchone()

    return book   

def edit_book():
    book = get_book()
    print(book)
    book_id = book[0]
    name_book = input("new name: ")

    cursor.execute("UPDATE books_table SET name =? WHERE book_id = ?", (name_book, book_id))
    conn.commit()

        

 

    

def save_books():
    with open('book.json', 'w', encoding='utf-8') as file:
        json.dump(list_book, file, ensure_ascii= False, indent=4)



#начинается выполнение программы 
#читать
with open('book.json', 'r', encoding='utf-8') as file:
    list_book = json.load(file)


message = input("add/get/edit:  ")
if message == "add" :            
    add_book()

if message == "get" :
    get_book()

if message == "edit" :
    edit_book()



    
save_books()


    