from flask import Flask, render_template, jsonify
from os import listdir
from os.path import join, abspath, dirname
from typing import List
from flask_socketio import SocketIO

ROOT_DIR = dirname(abspath(__file__))
STATIC_DIR = join(ROOT_DIR, 'static')

app = Flask(__name__)
socketio = SocketIO(app)
students = None


class Student:

    def __init__(self, student_id: int, name: str, major: str,
                 image_path: str):
        self.id = student_id
        self.name = name
        self.major = major
        self.image_path = image_path


@app.route('/')
def show(**kwargs):
    return render_template('show.html', students=students,
                           async_mode=socketio.async_mode, **kwargs)


@app.route('/settings')
def settings(**kwargs):
    return render_template('settings.html', students=students,
                           async_mode=socketio.async_mode, **kwargs)


@socketio.on('start')
def start():
    print('start')
    socketio.emit('start')


@socketio.on('stop')
def stop(message):
    print('stop')
    socketio.emit('stop', {'winner': message['winner']})


@socketio.on('students')
def students():
    print('students')
    socketio.emit('students', {'students': students})


@socketio.on('connect')
def on_connect():
    print('Client connected')


@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    """
    Image file names are expected to have the form
    <name> "_" [<name> "_"]* <major> "." <suffix>
    """
    images: List[str] = listdir(join(STATIC_DIR, 'students'))
    students = list()
    for index, image in enumerate(images):
        *name, major = image.split('.')[0].split('_')
        student = Student(index, ' '.join(name),
                          major, f'static/students/{image}')
        students.append(student.__dict__)
    socketio.run(app, port=5000)
