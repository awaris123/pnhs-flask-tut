from flask import Flask, render_template, request, redirect, url_for

'''
We create an instance of an object called 'Flask' from the flask library
'''
app = Flask(__name__)

'''
In python this is what call a dictionary or a hashtable which is a key/value store, it's how were going to store our data for this tutorial

This dict is actaully special becuase its a nested hashtable, where the value is actaully another dict
 Simmilar to a two dimensional array but with dictionaries
'''

fakeDB = {

    "user1":{
        "username":"Spiderman",
        "id" : 1
    },

    "user2":{
        "username":"Hulk",
        "id" : 2
    },

    "user3":{
        "username":"Wolverine",
        "id" : 3
    }
}




'''
The home page when we first access our application
Dont get intimidated by the decorater, its simply a function that takes in another function, which is the one we write directly underneath
The flask object has a method called route, i.e(app.route) which is how were going to define what goes on at different areas of our application or websitehe 


The first paramter we see is a slash, this defines the actual location of the logic going on at our application

The second paramter is a list which holds a string typhat defines that type of request that will be handled

There are many types of requests when dealing with HTTP however only 4 of them are most commonly used:
 - GET     -> This is what we use when we want to read or get data
 - POST    -> This is what we use when we want to create new data
 - PUT     -> This is what we use when we want to update or change data
 - DELETE  -> This is what we user when we want to delete data

The third parameter is implict, and it's the function that we wrote
'''

@app.route("/", methods = {"GET"})
def index():
    return "<h1>hello world!<h1>"




''' 
We can see here that "routes" can let us view information about the state of the application
'''
@app.route("/home", methods = {'GET'})
def greetHero():

    user = fakeDB
    title = "Home Page"
    return render_template('home.html', user=user, title=title)


'''
But we can also create or POST data to change the state of the application
'''
@app.route("/home", methods={"POST"})
def createHero():
    payload = request.form["user"]
    numHeros = len(fakeDB) + 1
    key = "user" + str(numHeros)

    fakeDB[key] = {
        "username": payload,
        "id" : numHeros
    }
    for hero in fakeDB.values():
        print(hero["username"], hero["id"])
    
    return redirect(url_for("greetHero"))
    


'''
For those of you akin to Java this is kind of but not exactly "public static void main(String[] args){}"
'''
if __name__ == "__main__":

    # Remeber that Flask object? it has a method called run which actaully runs our application
    app.run(debug=True)














