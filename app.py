from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

#connection string to mongoDB
app = Flask(__name__)
client = MongoClient("mongodb+srv://new-user2-admin:new-user2-admin@cluster0.uycxdcq.mongodb.net/?retryWrites=true&w=majority")

db = client.db
todos = db.todos

#Application route that controls the return statements
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

# ...

# delete function
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
