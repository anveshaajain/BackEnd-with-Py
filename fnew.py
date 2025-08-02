from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    # return "Wlecome to Anvesha's Worlddd stay happy and healthy"
    # return "ANVESHA JAIN!!!"
    return "I am coder and student of cloud tech!!"
    # return 'Hello %s!' % name
    # msg = '<h1>Hello %s! </h>' % name 
    # msg += '<p> Wlecome to Flask! </p>' 
if __name__ == '__main__':
    app.run()