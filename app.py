from flask import Flask
app =  Flask(__name__)
import db

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb app home page!"
@app.route("/connection")
def connect():
    new_brand = {'name' : 'Nike', 'name' : 'Puma'}
    db.brandnames.insert_one(new_brand)
    return "connected to the data base!"
if __name__=='__main__':
    app.run(port=8000)

