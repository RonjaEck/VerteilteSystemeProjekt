

################################################################################
#           file_service.py
#
#   1) Allow local upload of certificate file and save to mongodb
################################################################################


import os
import hashlib
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pymongo
from pymongo import MongoClient
from bson.json_util import loads, dumps


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def send_file_to_nodes(file):
#     print("122")
#     try:
# 	    return send_file('node_B.py', attachment_filename=file)
#     except Exception as e:
# 	    return str(e)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fname = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fname)
            md5_hash = hashlib.md5()
            # Direkt mit "file" von oben ?? Kommt drauf an, was wir mit dem File machen ... eindeutiger Name ? Archiv ?
            the_file = open(fname, "rb")
            content = the_file.read()
            md5_hash.update(content)
            digest = md5_hash.hexdigest()
            print("digest " + digest)
            the_file.close()
            new_filename =  digest + ".pdf"
            #send_file_to_nodes(the_file)
           
            
            os.rename(fname, os.path.join(app.config['UPLOAD_FOLDER'],new_filename)) # TODO = abfangen wenn file bereits umgewandelt und gespeichert wurde -> sofort öffnen (mit try und except?)
            # except:
            #     print("fehler")
            #     return redirect(url_for('download_file', name=new_filename))
            
# Cloud-DB
            #uri = "mongodb+srv://reck:B3r9WpA9IZUuastB@books.qbrpu62.mongodb.net/?retryWrites=true&w=majority"
                  #"mongodb+srv://cluster0.q3ydq.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
            #print(uri);
            #client = MongoClient(uri,
            #	tls=True)
            #print(client)
            #uri2 = "mongodb+srv://reck:topK1@database@certificates.0tltqqm.mongodb.net/?retryWrites=true&w=majority"
            #client2 = MongoClient(uri2, tls=True)
            	# tlsCertificateKeyFile='./atlas.pem') topK1@database
            #pymongo.MongoClient("mongodb+srv://reck:B3r9WpA9IZUuastB@books.qbrpu62.mongodb.net/?retryWrites=true&w=majority")
# oder lokal ...
            all_nodes =  ["http://localhost:21017/", "http://localhost:21018/" , "http://localhost:21019/" ]

            client=MongoClient("localhost", 21017) 
            # client=MongoClient("mongodb://reck:B3r9WpA9IZUuastB@localhost:21017,localhost:21018,localhost:21019/flask_db?ssl=true&authSource=admin&replicaSet=rHost&retryWrites=true&w=majority")

#client = pymongo.MongoClient("mongodb+srv://reck:topK1@database@certificates.0tltqqm.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
            #print("Hier1")
            #db = client['books']
            db = client.flask_db
            #db2 = client2['certificates']
            # print("Hier2")
            # collection = db['certificates']
            collection = db['todos']
            # collection2 = db2['certificates']
            # print("Hier3")
            print(collection.count_documents({}))
            doc = {'email':request.form["email"], 'name':request.form["name"], 'program':request.form["program"], 'filename':new_filename,'md5':digest}
            id = collection.insert_one(doc)
            # id2 = collection2.insert_one(doc)
            print(collection.count_documents({}))
            other_nodes = []
            for node in all_nodes:
                if node != request.base_url:
                    other_nodes.append(node)

            return redirect(url_for('download_file', name=new_filename))
    return '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
    <table>
    <tr><td>Name:</td><td><input type=text name="name"></td></tr>
    <tr><td>email:</td><td><input type=text name="email"></td></tr>
    <tr><td>Studiengang:</td><td><input type=text name="program"></td></tr>
    <tr><td>Token:</td><td><input type=text name="Token"></td></tr>
    <tr><td>Zeugnis(pdf):</td><td><input type=file name=file></td></tr>
    <tr><td colspan=2 halign=center><input type=submit value=Upload></td></tr>
    </table>
</form>
'''
    
app.run()
