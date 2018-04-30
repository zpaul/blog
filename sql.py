#add user
from uuid import uuid4
user =User(id=str(uuid4()),username='paul',password='abc')
db.session.add(user)
db.session.commit()

#add post
post_one = Post('First Post')
post_one.id = str(uuid4())
post_one.user_id = user.id
db.session.add(post_one)
db.session.commit()

#add user->post
user = db.session.query(User).first()
post_second = Post('Second Post')
post_second.id = str(uuid4())
post_second.users = user
db.session.add(post_second)
db.session.commit()

#tags
tag_one = Tag('life')
tag_one.id=str(uuid4())
tag_two=Tag('sports')
tag_two.id=str(uuid4())
tag_three=Tag('falsk')
tag_three.id=str(uuid4())
posts=db.session.query(Post).all()
post_one = posts[0]
post_two=posts[1]
post_one.tags=[tag_two]
post_two.tags=[tag_one,tag_two,tag_three]
db.session.add(post_one)
db.session.add(post_two)
db.session.commit()

#append tags to post
tag_one.posts.all()
tag_one.posts.append(post_one)


#Alembic
python manage.py db
python manage.py db init
python manage.py db migrate -m "Initial migration"
python manage.py db upgrade
python manage.py db history
python manage.py db downgrade <history_id>
