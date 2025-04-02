from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    # Query tasks by category
    then_tasks = Task.query.filter_by(category='Then').all()
    now_tasks = Task.query.filter_by(category='Now').all()
    later_tasks = Task.query.filter_by(category='Later').all()
    return render_template('index.html', then_tasks=then_tasks, now_tasks=now_tasks, later_tasks=later_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form.get('description')
    category = request.form.get('category')  # Expected to be 'Then', 'Now', or 'Later'
    if description and category:
        new_task = Task(description=description, category=category)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        # Toggle the task status
        task.status = not task.status
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
        # Create tables before running the server
    with app.app_context():
        db.create_all()
    app.run(debug=True)