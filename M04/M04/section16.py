"""
Reed Peglow
SDEV 220
M04 Programming Assignment - Modules and Databases
Section 16"""


#16.3 Create a CSV file called books2.csv by using these lines:

book_info = """title, author, year
The Weirdstone of Brisingamen, Alan Garner, 1960
Perdido Street Station, China Miéville, 2000
Thud!, Terry Practchett, 2005
The spellman Files, Lisa Lutz, 2007
Small Gods, Terry Preatchett, 1922
"""

with open("books2.csv", "wt") as outfile:   #context manger
    outfile.write(book_info)

#16.4 Use the sqlite3 module to create a SQLite database called books.db 
#and a table called books with these fields: title (text), author (text), and year (integer).

import sqlite3                               
database = sqlite3.connect("books.db")   #connect database to sqlite
pointer = database.cursor()              #point at database
pointer.execute('''CREATE TABLE book(tittle text, author text, year int)''')  #create staments in SQL
database.commit()                        #save

#16.5 Read books2.csv and insert its data into the book table.
import csv
import sqlite3
add_data = "insert its data into the book table(?,?,?)"     #add data where ? are place holders
with open("books2.csv", "rt") as infile:                     
    books = csv.DictReader(infile)
    for book in books:
        pointer.execute(add_data, (books["title"], books["author"], books["year"])) #add info from DictReader infile called books
        
database.commit()     #save

#16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 8.6. 
# As in 8.8, select and print the title column from the book table in alphabetical order.

import sqlalchemy
connect = sqlalchemy.create_engine("sqlite:///books.db")
statements = "SELECT title FROM book ORDER BY title ASC"
setups = connect.execute(statements)
for setup in setups:
    print(setup)
