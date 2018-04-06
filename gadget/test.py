#return statment within for loop
#also going to test the database to determine what the main problem of the gadget program

from database import Database
def test():

    data = ('something',112,'a',11)

    for new in data:
        return new




newData = test()

#print(len(newData))
data = Database()
print(data.get_all())
print(data.get_one('database viewer'))
#PROBLEM : the database is not returning any of the data and only returning "[]" without the quotes
#POSSIBLE SOLUTION : dont use double quotes, only singular ones
#update : single quote is still not returning the data, maybe its the format?
#maybe change the database on line 45 from fetchall to fetchone?

#data is returning tuple of tuples, changed it to only return the data in its natural format
#now data is a list of tuples


#data needs to be a singular tuple, or is the search feature not working?...
#SOLVED : the problem was the method get_one() parameter name had to be different from the column name


