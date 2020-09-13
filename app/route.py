from flask import Blueprint , request , render_template, url_for
from .model import Todo

todo = Blueprint("tasks",__name__)

@todo.route('/') 
def show(): 
    incomplete = Todo.query.filter_by(complete=False).all() 
    complete = Todo.query.filter_by(complete=True).all() 
  
    return render_template('index.html', incomplete=incomplete, complete=complete) 
  
  
@todo.route('/add', methods=['POST']) 
def add(): 
    todo = Todo(text=request.form['todoitem'], complete=False) 
    db.session.add(todo) 
    db.session.commit() 
  
    return redirect(url_for('show')) 
  
  
@todo.route('/finish/<id>') 
def finish(id): 
  
    todo = Todo.query.filter_by(id=int(id)).first() 
    todo.complete = True
    db.session.commit() 
  
    return redirect(url_for('show')) 