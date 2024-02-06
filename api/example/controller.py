import mysql.connector as mysql
from shared.connection import db

def get_message(id):
    # row = db.session.query(MyModel).filter(MyModel.id == id).first()
    return{}
    # cursor = db.cursor()
    # res = cursor.execute('SELECT * FROM messages WHERE id = ?', (id,)).fetchone()
    # cursor.close()
    # return dict(res) if not res is None else None

def save_message(adict):
    # row = db.session.query(MyModel).all()
    return {}