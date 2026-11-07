import pandas as pd

workout_data = None


def load_data():
    global workout_data
    try:
        workout_data = pd.read_csv('files/workout_data.csv', index_col='workout')
    except FileNotFoundError:
        print('ERROR: Unable to load workout data')


def save_data():
    global workout_data
    try:
        workout_data.to_csv('files/workout_data.csv')
    except (PermissionError, FileNotFoundError):
        print('ERROR: Unable to save workout data')
