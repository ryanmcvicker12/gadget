#app for all my ideas
#should be nicely styled after the app is up and WORKING
#should allow me or other users to create accounts?
#should allow the user to submit pictures/sketches/websites or any places where they found this idea
#ryan mcvicker
from database import Database
from flask import Flask, render_template,redirect,request, url_for
import sqlite3
#project is on github now
#how to upload, send, and display pictures while adding them to sqlite3 database
#how to allow users to create accounts
#how to send picture to and email


#forms: form to send all data to the database
#form to add new picture
#form to search for certain gadget
#form to

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/submittedData', methods=['POST'])
def submittedData():#method to send all data to the database and redirect user to the homepage
    d = Database()
    d.add_to(request.form["name"],request.form["description"],request.form["genre"],request.form["timegoal"])
    return redirect('/')


@app.route('/searchPage') #webpage for searching ideas
def searchPage():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    data = Database()
    theName = request.form["name"] #gets data from the form
    gadgetData = data.get_one(theName)
    #have to check in case values are none
    #the values are showing up as none

    print(gadgetData)
    print('length of data :{}'.format(len(gadgetData)))

    #turn data into dictionary

    #dataDictionary = [gadgetData[0],gadgetData[1],gadgetData[2],gadgetData[3]]


    return redirect('/getdata/{}/{}/{}/{}'.format(gadgetData[0],gadgetData[1],gadgetData[2],gadgetData[3])) #pass in list as argument?
    #return redirect('/')

#may have to encrypt some values in order to make the app more secure
@app.route('/getdata/<string:name>/<string:description>/<string:genre>/<string:timegoal>')
#@app.route('/getdata/<userData>') #argument that is a list that has no type?
def getdata(name,description,genre,timegoal):

    return render_template('showdata.html', name=name,genre=genre,description=description,timegoal=timegoal)





if __name__ == '__main__':
    app.run(debug=True,port=7000)
