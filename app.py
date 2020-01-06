
'''
Python/Flask tutorial for PNHS AP CS students CRUD API
'''
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from models.hero import Hero

app = Flask(__name__)



cred = credentials.Certificate(r"heroes-api-tut-b2bc9-firebase-adminsdk-qqinz-da035f84c1.json")
fb_app = firebase_admin.initialize_app(cred, {

    "databaseURL":"https://heroes-api-tut-b2bc9.firebaseio.com/"
})

@app.route("/api/heroes", methods = {'GET'})
def greetHero():
    headRef= db.reference('')
    lst = list(headRef.get())
    res = str(lst[::-1])
    return jsonify(res), "200"
    

@app.route("/api/heroes/<hero>", methods = {'GET'})
def whichHero(hero):
    try:
        headRef= db.reference('')
        for description in list(headRef.get())[1::]:
            if description["name"] == hero:
                res = description

        return jsonify(res), "200"
        
    except:
        pass

    return "404"

@app.route("/api/heroes", methods={"POST"})
def createHero():

    try:
        headRef= db.reference('')
        hero = Hero(request.json["user"]).toDict()
        nextNum = len(list(headRef.get()))
        headRef.child(hero["name"]).set(hero)


        return "200"

    except:
        return "500"

@app.route("/api/heroes", methods={"PUT"})
def changeHero():
    try:
        hero = request.json["user"]
        toBeChanged = request.json["attr"]
        newValue = request.json["value"]

       
        if toBeChanged != "origin" and toBeChanged != "power":
            1 / 0

        heroRef = db.reference(hero)

        if heroRef:
            heroRef.update({
              toBeChanged : newValue  
            })
            print(heroRef.get())

        else:
            1 / 0


        return "200"
    
    except:
        return "500"
    


@app.route("/api/heroes", methods={"DELETE"})
def killHero():  
    try:  
        hero = request.json["user"]
        toDel = db.reference(hero)
        if toDel:
            toDel.delete()
        else:
            1 / 0

        return "200"


    except:
        return "500"


if __name__ == "__main__":

    app.run(debug=True)














