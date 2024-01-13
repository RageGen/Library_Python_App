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

After finishing your postgre install go to the repository file postgresql_commands.py and on the first line:
   
    conn = psycopg2.connect(dbname='', host='', user='', password='')
   
Add your database name, host, user and password all inside quotes, by default your info should look like this:
             
    conn = psycopg2.connect(dbname='template0', host='localhost', user='postgres', password='Password you added on install')

In addition, create tables in your newly created database, all the necessary tables are reflected in the tables.sql file.

### How to run it

We have two options on how to run it:
 
 1- The fast way is just opening the main_file.py on your IDE and running it 
(make sure both files are on the same folder).
 
 2- We can use pyinstaller to make a .exe file (this makes it better for 
the people that will constantly be using it, since after creating a .exe the 
only thing needed to run is to double click the file).

Lets make a .exe file. On your terminal type:

        pip install pyintaller
        
After installing pyinstaller go to the file directory on your terminal and type:

     pyinstaller --onefile -w main_file.py



## Using the GUI

Here are some examples with what you can do with the GUI:


- Inserting data
![Insert](https://github.com/RageGen/Library_Manage_Python_Project/assets/82442165/6f53656d-7843-4fe8-83bf-c7fb164d5470)

- Deleting data
![Delete](https://github.com/RageGen/Library_Manage_Python_Project/assets/82442165/751a1ee0-9348-4c3c-a5a6-925371c6af81)

- Updating data
![Update](https://github.com/RageGen/Library_Manage_Python_Project/assets/82442165/7c58a3ec-371f-4b48-ba0a-c89f564f17ba)

- AVG Cost
![Cost](https://github.com/RageGen/Library_Manage_Python_Project/assets/82442165/f2b19dae-2d16-4b8f-bf26-85459d780a15)

- Expired readers
![Readers](https://github.com/RageGen/Library_Manage_Python_Project/assets/82442165/c150d6af-a58a-45a9-8a09-97f6b8006b04)




