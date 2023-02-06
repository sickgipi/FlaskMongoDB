from flask import Blueprint, render_template, request, redirect, url_for

from .extensions import mongo

main = Blueprint('main', __name__)

todos_collection = mongo.db.todos
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo = request.form.get('todo')
    todos_collection.insert_one({'testo': todo, 'completato': False})
    return redirect(url_for('main.index'))