
'''
Python/Flask tutorial for PNHS AP CS students
'''
from flask import Flask, render_template, request, redirect, url_for
from models.hero import Hero



'''
We create an instance of an object called 'Flask' from the flask library which represents our application.
We take in a "special python variable" that is always defined for every python script -> __name__
The __name__ variable is special becuase, it's value depends on how we run this program,

There are two ways to run any python program:

    - We execute it directly, i.e( python3 app.py )
    - We import this script into another python file and use it's functions/objects

If we run this program directly then  __name__ is == "__main__"
If we import this script then __name__ == to whatever the name of the script is, in this case: "app"

'''

app = Flask(__name__)
app.counter = 3



'''
---------------------------------------------------------------------------------------------------------------------------------------------

In python this is what call a dictionary or a hashtable which is a key/value store, it's how were going to store our data for this tutorial

ex. heroes = {

    "peter parker" : "Spiderman",
    
    "tony stark"  : "Iron Man",

    "steve rodgers" : "Captain America"

}

We can index this data structure as so:

heros["peter parker"]

This yields - > "Spiderman"

We can also create new key value pairs as so:

heros["bruce banner"] = "hulk"

Finally we can delete key value pairs as such:

del heroes["peter parker"]

this will remove that mapping from the dictionary

----------------------------------------------------------------------------------------------------------------


Normally we would actaully create a database connection with a database url, however for the sake of time and simplicty we will use a data structure
There exist databases that have this similar Key Value stucture


This dict is actaully special becuase its nested, where the value is actaully another dict
'''

hero1 = Hero("mysterio").toDict()
hero2 = Hero("quicksilver").toDict()
hero3 = Hero("megaman").toDict()


fakeDB = {

    1:hero1,

    2:hero2,

    3:hero3
}

title = "Home Page"





'''
The home page when we first access our application
Dont get intimidated by the decorater, its simply a function that takes in another function, which is the one we write directly underneath
The flask object has a method called route, i.e(app.route) which is how were going to define what goes on at different areas of our application or website


The first paramter we see is a slash, this defines the actual location of the logic going on at our application

The second paramter is a list which holds a string typhat defines that type of request that will be handled

There are many types of requests when dealing with HTTP however only 4 of them are most commonly used:

 - GET     -> This is what we use when we want to read or get data
 - POST    -> This is what we use when we want to create new data
 - PUT     -> This is what we use when we want to update or change data
 - DELETE  -> This is what we user when we want to delete data

The third parameter is implict, and it's the function that we wrote underneath the decorator
'''

@app.route("/", methods = {"GET"})
def index():
    return "<h1>hello world!<h1>"



''' 
We can see here that "routes" can let us view information about the state of the application via a GET request
'''
@app.route("/home", methods = {'GET'})
def greetHero():

    title = "Home Page"
    return render_template('home.html', heroes=fakeDB, title=title)

'''
If we want to look at or GET a specific resource (in this case our heroes are the resource), 
we can pass in parameters through the header of the url,
this is called passing parameters through the header 
NOTE: in the decoratoer we take a parameter 'hero' is in carrot brackets, this denotes a header parameter which flask implicitly passes to our function as an argument
'''
@app.route("/home/<hero>", methods = {'GET'})
def whichHero(hero):
    try:
        
        # This loop will iterate through our dictionary, we have to use two variables instead one to unpack the key/val pair from the dict
        for descriptions in fakeDB.values():
            if descriptions["name"] == hero:
                tmp = descriptions

        return render_template('profile.html', hero = tmp, title = title)
    except:
        print("AHH")
        pass

    return redirect(url_for("greetHero"))

'''
But we can also create or POST data or a resource, we pass in paramters through the BODY of the request,
this is different than the header as we saw previously, becuase the this data is 'hidden' and not passed through the URL
'''
@app.route("/home", methods={"POST"})
def createHero():
    print(request.json)
    payload = request.json["user"]
    newHero = Hero(payload)
    print(newHero)
    app.counter += 1
    fakeDB[app.counter] = newHero.toDict()

    
    return redirect(url_for("greetHero"))


'''
The Put method here takes in two paramteters in the request body
a  hero that will be changed
and the new hero that will replace it
'''
@app.route("/home", methods={"PUT"})
def changeHero():
    try:
        toBeChanged = request.json["user"]
        newUser = request.json["newUser"]
        print(toBeChanged, newUser)
        for key, value in fakeDB.items():
            if  value["name"] == toBeChanged:
                fakeDB[key] = Hero(newUser).toDict()
 
    except:
        pass
    
    return redirect(url_for('greetHero'))


'''
This delete method will, take in a hero as a parameter and then delete or "kill" that hero
'''
@app.route("/home", methods={"DELETE"})
def killHero():  
    try:  
        payload = request.json["user"]
    
        toDel = ""
        for key, value in fakeDB.items():
            if value["name"] == payload:
                toDel = key
                break
        del fakeDB[toDel]

    except:
        pass

    return redirect(url_for("greetHero"))
    


'''
For those of you akin to Java this is kind of but not exactly "public static void main(String[] args){}"
'''
if __name__ == "__main__":

    # Remeber that Flask object? it has a method called run which actaully runs our application
    app.run(debug=True)














