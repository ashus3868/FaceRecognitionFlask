from flask import Flask

app=Flask(__name__)


@app.route('/')
def message():
    return "<h1>Hello World</h1>"

@app.route('/hello')
def second_page():
    return "<h2>This is a testing api for routing. Innovate Yourself</h2>"

@app.route('/hello/<float:name>')
def Dynamic_api(name):
    return "<h2>Hello {}</h2>".format(name)

#save time and
if __name__=="__main__":
    app.run(debug=True)