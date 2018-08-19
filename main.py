from flask import Flask, url_for, render_template
from os import listdir
from os.path import join, abspath, dirname
from typing import List

ROOT_DIR = dirname(abspath(__file__))
STATIC_DIR = join(ROOT_DIR, 'static')

app = Flask(__name__)


class Student:

    def __init__(self, student_id: int, name: str, major: str,
                 image_path: str):
        self.id = student_id
        self.name = name
        self.major = major
        self.image_path = image_path

    @property
    def serialize(self) -> dict:
        return {
                'id': self.id,
                'name': self.name,
                'major': self.major,
                'image_path': self.image_path
        }


def init():
    """
    Filenames are expected to have the form
    "<surname>_<name>_<major>.<suffix>"
    """


@app.route('/')
def show(**kwargs):
    return render_template('show.html', **kwargs)


@app.route('/settings')
def settings(**kwargs):
    return render_template('settings.html', **kwargs)


@app.route('/students', methods=['GET'])
def students():
    images: List[str] = listdir(join(STATIC_DIR, 'students'))
    students: List[dict] = list()
    for index, image in enumerate(images):
        surname, name, major = image.split('.')[0].split('_')
        student = Student(index, f'{surname} {name}', major, image)
        students.append(student.serialize)
    return repr({'students': students})


@app.route('/start', methods=['POST'])
def start():
    pass


@app.route('/stop/<id>', methods=['POST'])
def stop(id: int):
    pass


@app.route('/static/<filepath>', methods=['GET'])
def static_files(filepath):
    return url_for('static', filename=filepath)


if __name__ == '__main__':
    init()
    app.run(host='localhost', port='8080', debug=True)
