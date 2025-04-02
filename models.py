from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(20), nullable=False)  # 'Then', 'Now', 'Later'
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.description} ({self.category})>'