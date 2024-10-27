import json 
import sqlite3

conn = sqlite3.connect("sqlite/Base_Books.db")
cursor = conn.cursor()


def add_book():
    name = input("name: ")
    author_name = input("author: ")

    cursor.execute("SELECT author_id FROM authors_table WHERE name = ? ", (author_name,))
    author_row = cursor.fetchone()
    author_id = author_row[0]

    # rating = input("rating: ")
    # characterictic = input("characterictic: ")
    
    # book = {"name": name, "author": author, "rating": rating, "characterictic": characterictic}
    # list_book.append(book)

    cursor.execute("""
                   INSERT INTO books_table (name, author_id) VALUES (?, ?)
                   """,
                    (name, author_id))
    conn.commit()

#выбрать
def get_book():
    search_word = input("search: ")
  
    for book in list_book:
        if search_word in book["name"] or search_word in book["author"]:
            print(book)
            return book

def edit_book():
    book = get_book()
    key = input("edit: ")
    key in book.keys()
    if key in book.keys():
        book[key] = input(key + ' :')
    else:
        answer = input("add key?" )
        if answer == "yes":
            book[key] = input(key + ' :')

def add_keytoallbooks():
    key = input("edit all: ")
    for book in list_book:
        book[key] = input(key + ' :')
        

 

    

def save_books():
    with open('book.json', 'w', encoding='utf-8') as file:
        json.dump(list_book, file, ensure_ascii= False, indent=4)



#начинается выполнение программы 
#читать
with open('book.json', 'r', encoding='utf-8') as file:
    list_book = json.load(file)


message = input("add/get/edit/edit all:  ")
if message == "add" :            
    add_book()

if message == "get" :
    get_book()

if message == "edit" :
    edit_book()

if message == "edit all" :
    add_keytoallbooks()

    
save_books()


    