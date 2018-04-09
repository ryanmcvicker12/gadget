import sqlite3





#adjust the class accordingly
#should be used to store alot more data which i should list them below.
"""        DATABASE SCHEMA            
 
 
 
 table name TEXT,description TEXT, genre TEXT, picture ???, time goal TEXT,
 
 
 NOTE: atm just creating the easy components with only text information to be added 
 
 
 
 
 """
class Database:

    def __init__(self):
        self.conn = sqlite3.connect('gadget.db')

        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS ideas(name TEXT,description TEXT, genre TEXT, timegoal TEXT)')
    def add_to(self,name,description,genre,timegoal):
        try:
            self.c.execute("INSERT INTO ideas VALUES(?,?,?,?)", (name,description,genre,timegoal))
            print('data added successfully')
            self.conn.commit()
        except Exception as e:
            print(e)
            print("data couldent be added")

    def get_all(self):# should return all data in the database to the user in a formatted way
        self.c.execute("SELECT * FROM ideas")
        return self.c.fetchall() #returns the data to the app


    def get_one(self,title):# this method should be for the user to search for a specific task

        self.c.execute("SELECT * FROM ideas WHERE name = ?", (title,)) #should grab certain

        return self.c.fetchone()

        #close the connection? why?
