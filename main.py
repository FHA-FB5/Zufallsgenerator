from flask import Flask, url_for, render_template, jsonify
from os import listdir
from os.path import join, abspath, dirname
from typing import List
import websockets
import asyncio
import json
from threading import Thread

ROOT_DIR = dirname(abspath(__file__))
STATIC_DIR = join(ROOT_DIR, 'static')

app = Flask(__name__)
client = None
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
    return render_template('show.html', **kwargs)


@app.route('/settings')
def settings(**kwargs):
    return render_template('settings.html', **kwargs)


@app.route('/students', methods=['GET'])
def students():
    return jsonify({'students': students})


@app.route('/start', methods=['GET'])
async def start():
    await client.send(json.dumps({'type': 'start'}))


@app.route('/stop/<id>', methods=['GET'])
async def stop(id: int):
    winner = next(student for student in students if student['id'] == id)
    await client.send(json.dumps({'type': 'stop',
                                  'winner': winner['name']}))


async def handler(websocket, path):
    client = websocket


@app.route('/static/<filepath>', methods=['GET'])
def static_files(filepath):
    return url_for('static', filename=filepath)


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

    def websocket_server():
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(handler, 'localhost', 6666)
        )
        asyncio.get_event_loop().run_forever()

    Thread(target=websocket_server).start()
    app.run(host='localhost', port=8080, debug=True)