'''
Node A 
    Primary
    ---> connect_to_database books
    Funktion upload_file
    Funktion allowed_files
    Funktion download_file
    Todo: send_copy_to_Nodes (Node B, C, D, E)
    Todo: show_user_if_all_nodes_got_the_uploaded_files()
Node B
    Secondary
    ---> connect_to_database certificates
    Funktion get_copy_of_file(file)
    Funktion save_file_in_database(file)
    Funktion send_apply()




'''
from distutils.log import debug
import sys
from flask import Flask, render_template, request, url_for, redirect
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

# def connect_to_databse():
#     uri = "mongodb+srv://reck:h1ellod2ute@certificates.0tltqqm.mongodb.net/?retryWrites=true&w=majority"
#     client = MongoClient(uri, tls=True)
#     db = client['certificate-copy']
#     collection = db['certificate-copy']
#     print(collection.count_documents({}))
#     doc = {'email': 'dumongo', 'name':'dumongo', 'program':'dumongo', 'filename':'dumongo','md5':'dumongo'}
#     id = collection.insert_one(doc)
#     print(collection.count_documents({}))

# def get_copy_of_file():
#     file = request.get(file)
#     response = request.post(url="http://0.0.0.0:5000",data=file)
#     print(file)

# @app.route('/')
# def index():
#     connect_to_databse()
#     get_copy_of_file()
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=81)
#     #app.run(debug=True)

client = MongoClient("localhost", 21017)

db = client.flask_db



todos = db.tools

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

app.run(debug=True)