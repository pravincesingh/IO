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
            # L1="Light 1 is "+db.child("Lights").child("light1").get().val()
            # L2="Light 2 is "+db.child("Lights").child("light2").get().val()
            return render_template("smart.html",L1=L1,L2=L2)
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    
    L1="Light 1 is "+db.child("Lights").child("light1").get().val()
    L2="Light 2 is "+db.child("Lights").child("light2").get().val()
    return render_template("smart.html",L1=L1,L2=L2)


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
            AM ="Advance mode is "+ db.child("AdvanceMode").child("mode").get().val()
            return render_template("advance.html",AM=AM)
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    AM ="Advance mode is "+ db.child("AdvanceMode").child("mode").get().val()
    return render_template("advance.html",AM=AM)


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    app.run()


     
   