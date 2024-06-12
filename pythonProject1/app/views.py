from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User
import requests
from app.services import create_user, get_all_users # update_user_first_name, delete_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name')
def name():
    return "Patrycja Przybysz"

@app.route('/add_numbers', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        number1 = request.form['number1']
        number2 = request.form['number2']
        result = int(number1) + int(number2)
        return f'Wynik: {result}'
    return render_template('form.html')

# 4 pierwsze zdj
@app.route('/photos')
def photos():
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    photos = response.json()[:4]
    return render_template('photos.html', photos=photos)

# wyswietla 3 4 i 5 zdjęcie
# @app.route('/photos')
# def photos():
#     photo_ids = [3, 4, 5]
#     photos = []
#     for photo_id in photo_ids:
#         response = requests.get(f'https://jsonplaceholder.typicode.com/photos/{photo_id}')
#         if response.status_code == 200:
#             photos.append(response.json())
#     return render_template('photos.html', photos=photos)



@app.route('/create_user', methods=['GET', 'POST'])
def create_user_view():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        create_user(first_name, last_name)
        return redirect(url_for('get_all_users_view'))
    return render_template('create_user.html')

@app.route('/get_all_users')
def get_all_users_view():
    users = get_all_users()
    return render_template('users.html', users=users)



# @app.route('/update_user')
# def update_user_view():
#     update_user_first_name('John', 'Jane')
#     return 'Imię użytkownika zaktualizowane'
#
# @app.route('/delete_user')
# def delete_user_view():
#     delete_user('John')
#     return 'Użytkownik usunięty'
