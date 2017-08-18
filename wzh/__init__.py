from flask import Flask, redirect, url_for
from flask_admin import Admin
try:
	from .blog import blog
except:
	from blog import blog

try:
	from .blog.models import Post
except:
	from blog.models import Post

from flask_admin.contrib.mongoengine import ModelView


app = Flask(__name__)
app.register_blueprint(blog, url_prefix='/blog')
admin = Admin(app, name='blog', template_mode='bootstrap3', url='/blogadmin')




class PostView(ModelView):
	column_filters = ['title']

admin.add_view(PostView(Post))


if __name__ == '__main__':
	app.run(port=5000, debug=True)