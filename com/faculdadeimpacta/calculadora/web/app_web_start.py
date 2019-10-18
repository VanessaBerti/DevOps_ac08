from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
   return 'Index Page!'

if _name_ == '_main_':
   app.run()