
from app import env as env
import models.client as model 
import pyqrcode

class client_view():

	template = env.get_template('layout.html')
	data = model.DB('data.sqlite')

	@staticmethod
	def render_get_form()->str:
		
		s = client_view.template.render(title="Индексная страница", content="form.html")
		return s


	@staticmethod
	def render_post(body)->str:
		
		c = model.Client(body['first_name'][0], body['last_name'][0], body['mail'][0], body['city'][0], body['index'][0], body['address'][0])

		client_view.data.create()
		id = client_view.data.input_data(c)
		
		url = pyqrcode.create(f'http://localhost:8000/users/{id}/')
		url.svg(f'images/{id}.svg', scale=8)

		s = client_view.template.render(title="Данные получены", content="post.html", cl=c, id=id)
		return s

	
	@staticmethod
	def render_404()->str:

		s = client_view.template.render(title="Ошибка 404", content="404.html")
		return s

	
	@staticmethod
	def render_user_page(user, id)->str:

		cl = model.Client(user[1], user[2], user[3], user[4], user[5], user[6])

		s = client_view.template.render(title=f"{cl.full_name}", content="user.html", cl=cl, id=id)
		return s


	@staticmethod
	def render_all_users():

		users = client_view.data.get_all()
		s = client_view.template.render(title="Таблица пользователей", content="allusers.html", users=users)
		return s
