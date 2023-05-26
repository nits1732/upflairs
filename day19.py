from flask import Flask
app=Flask(__name__)

@app.route('/')
def sample():
    return 'kuch bhi nhi'


@app.route('/new')
def new():
    return '<h1> This is heading </h1>'

app.run(debug='True')






# @ decorator-kisi bhi ordinary fnc to extraordinary
