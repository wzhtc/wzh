from flask import Flask
from flask_admin import Admin
try:
	from .blog import blog
except:
	from blog import blog


app = Flask(__name__)
app.register_blueprint(blog, url_prefix='/blog')
admin = Admin(app, name='microblog', template_mode='bootstrap3')


if __name__ == '__main__':
	app.run(port=5000, debug=True)