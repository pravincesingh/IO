from flask import Flask, render_template ,request
# from sklearn.externals import joblib
import joblib
# from firebase import firebase
# firebase = firebase.FirebaseApplication('https://smartlightsystem-19c52.firebaseio.com/', None)

app =Flask(__name__)
#firebase
import pyrebase
config = {
    "apiKey": "AIzaSyBJV9POvfWm2P6FD-RohJGYIM8vj8loFOs",
    "authDomain": "pravince-8ac79.firebaseapp.com",
    "databaseURL": "https://pravince-8ac79.firebaseio.com",
    "projectId": "pravince-8ac79",
    "storageBucket": "pravince-8ac79.appspot.com",
    "messagingSenderId": "832471264141",
    "appId": "1:832471264141:web:685cd44192d88b8fa0abc4",
    "measurementId": "G-692GXPM601"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/smart.html", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('ON1') == 'ON':
                # pass
            db.child("Lights").update({"light1":"on"})
            print("Light on")
        elif  request.form.get('OFF1') == 'OFF':
                # pass # do something else
            db.child("Lights").update({"light1":"off"})
            print("Light off")
        elif request.form.get('ON2') == 'ON':
                # pass
            db.child("Lights").update({"light2":"on"})
            print("Light on")
        elif  request.form.get('OFF2') == 'OFF':
                # pass # do something else
            db.child("Lights").update({"light2":"off"})
            print("Light off")
        else:
                # pass # unknown
            return render_template("smart.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("smart.html")


@app.route("/advance.html", methods=['GET', 'POST'])
def advance():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('AON') == 'ON':
                # pass
            db.child("AdvanceMode").update({"mode":"on"})
            print("Light on")
        elif  request.form.get('AOFF') == 'OFF':
                # pass # do something else
            db.child("AdvanceMode").update({"mode":"off"})
            print("Light off")
        else:
                # pass # unknown
            return render_template("advance.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("advance.html")


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    app.run()


     
   