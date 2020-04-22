from flask import Flask, render_template, Response, request, redirect, url_for
import pymongo
import base64
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    cluster =MongoClient("mongodb+srv://DBKAILASH:dbkailash@cluster0-oilup.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["resume"]
    collection = db["coll_resume"]

    with open(r"C:\Users\TarunVashishth\Desktop\Futurero 2020 Batch resumes\tar23.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())

    abc=db.coll_resume.insert_one({"image":encoded_string})
    forward_message = "File Upload Successful"
    return render_template('index.html', forward_message=forward_message);

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)