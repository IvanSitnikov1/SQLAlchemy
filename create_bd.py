from app import app
from database import db, Book, Genre
import random
from datetime import datetime as DT
from datetime import timedelta



def get_random_date():
    delta = DT.strptime('01.01.2018', '%d.%m.%Y') - DT.strptime('01.01.2017', '%d.%m.%Y')
    return DT.strptime('01.01.2017', '%d.%m.%Y') + timedelta(random.randint(0, delta.days))

with app.app_context():
    db.drop_all()
    db.create_all()

    pr = Genre(name='Проза')
    ph = Genre(name='Фантастика')
    tr = Genre(name='Приключения')
    db.session.add(pr)
    db.session.add(ph)
    db.session.add(tr)
    books_dict = {
        '451° по Фаренгейту': pr,
        '1984': ph,
        'Мастер и Маргарита': pr,
        'Шантарамм': tr,
        'Цветы для Элджернона': ph
    }
    for i in range(10):
        for book, genre in books_dict.items():
            db.session.add(Book(name=book, added=get_random_date(), genre=genre))

    db.session.commit()