### Как запустить проект:

cd what_to_watch
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

Запустить проект:
```
flask run
```
pip install flask-sqlalchemy==3.1.1 

dialect+driver://username:password@host:port/database 

flask shell 
db.create_all()

opinion_1 = Opinion(title='Джой', text='Фильм обязателен к просмотру в ситуациях, когда кажется, что выхода нет, и всё летит в тартарары. Главная героиня придумала самоотжимающуюся швабру (невесть какое изобретение, казалось бы) и двигала свою идею всеми мыслимыми и немыслимыми путями. Да и актёрский состав интересен. Где ещё увидишь вместе Дженифер Лоуренс, Роберта де Ниро и Брэдли Купера.')
db.session.add(opinion_1)
db.session.commit()


# Применять только символы из набора ASCII? Нет!
app.json.ensure_ascii = False 

pip install Flask-WTF==1.2.1

pip install Flask-Migrate==4.0.7 
flask db init
flask db migrate -m "added added_by field" 
flask db upgrade