from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column('Date', db.Date)
    title = db.Column('Title', db.String())
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    link = db.Column('Link', db.Text)

    def __repr__(self):
        return f'''<Project (Date: {self.date}
                Title: {self.title}
                description: {self.description}
                Skills: {self.skills}
                Link: {self.link})>'''