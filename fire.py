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

AM ="Advance mode is "+ db.child("AdvanceMode").child("mode").get().val()
L1="Light 1 is "+db.child("Lights").child("light1").get().val()
L2="Light 2 is "+db.child("Lights").child("light2").get().val()
print(AM)
print(L1)
print(L2)