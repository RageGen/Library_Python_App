# User Friendly Postgresql Database GUI for Library Manage

A tkinter GUI with psycopg2 database adapter that runs the query and outputs info on the screen.
Useful for Library workers with no sql knowledge.

What it does: 
              
              - Display the database table.  
              - Insert data.                 
              - Update data.                 
              - Delete data.                       
              - Select data rows to edit.
              - The output of the average cost of books.
              - The withdrawal of people who have missed the deadline for the delivery of books.

### Requirements

- Python
- Tkinter module
- Psycopg2 module
- Re module

## Getting Started

Since this is a GUI to connect to a postgresql database you will need to have a postgresql database (You can use another 
sql language but you would need to change the adapter and tweak the code). 

Install Postgresql here: https://www.postgresql.org/

After finishing your postgre install go to the repository file postgresql_commands_*.py and on the first line:
   
    conn = psycopg2.connect(dbname='', host='', user='', password='')
   
Add your database name, host, user and password all inside quotes, by default your info should look like this:
             
    conn = psycopg2.connect(dbname='template0', host='localhost', user='postgres', password='Password you added on install')

In addition, create tables in your newly created database, all the necessary tables are reflected in the tables.sql file.

### How to run it

We have two options on how to run it:
 
 1- The fast way is just opening the main.py on your IDE and running it 
(make sure both files are on the same folder).
 
 2- We can use pyinstaller to make a .exe file (this makes it better for 
the people that will constantly be using it, since after creating a .exe the 
only thing needed to run is to double click the file).

Lets make a .exe file. On your terminal type:

        pip install pyintaller
        
After installing pyinstaller go to the file directory on your terminal and type:

     pyinstaller --onefile -w main.py



## Using the GUI

Here are some examples with what you can do with the GUI:


- Inserting data
![Insert](https://github.com/RageGen/Library_Python_App/assets/82442165/11918a05-9a92-42f5-8ae7-e334a41f7ef6)

- Deleting data
![Delete](https://github.com/RageGen/Library_Python_App/assets/82442165/e15119d0-24b4-4faa-809b-d8d3bee39fe5)

- Updating data
![Update](https://github.com/RageGen/Library_Python_App/assets/82442165/a3cfd1b5-b3ed-4ea0-a555-812322e33d62)

- AVG Cost
![Cost](https://github.com/RageGen/Library_Python_App/assets/82442165/80ba3216-6ce0-48de-93e0-70de132354d6)

- Expired readers
![Readers](https://github.com/RageGen/Library_Python_App/assets/82442165/52288e61-d192-4efe-add4-6a3ba6bb2b9e)





