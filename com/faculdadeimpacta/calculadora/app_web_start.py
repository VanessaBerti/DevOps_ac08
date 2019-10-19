from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
   return 'Index Page!'

if __name__ == '__main__':
   app.run()