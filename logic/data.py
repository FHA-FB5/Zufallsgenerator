import json
from pathlib import Path


def add_person(person, filepath: str):
    '''
    Add person to a json encoded file, create file if it doesn't exist
    
    Args:
        person:
            person to add to the json file
        filepath:
            path of the json file
    '''
    filepath = Path(filepath)
    if not filepath.exists():
        Path(filepath.parent).mkdir(parents=True, exist_ok=True)
        with filepath.open('w') as file:
            json.dump({}, file)
    with filepath.open() as file:
        data = json.load(file)
    people = data.get('people', [])
    people = people + [person]
    data['people'] = people
    with filepath.open('w') as file:
        json.dump(data, file, indent=4)


def create_person(name: str, surname: str, age: int, sex: bool, major: str=None, image: str=None):
    '''
    Create a dictionary describing a person

    Args:
        name:
            given name of the person
        surname:
            surname of the person
        age:
            age of the person
        sex:
            Sex of the person, True = female, False = male
        major:
            Major of the person
        image:
            filepath to an image of the person
    '''
    return {
        'name': name,
        'surname': surname,
        'age': age,
        'sex': sex,
        'major': major,
        'image': str(Path(image).absolute()) if image is not None else None
    }
