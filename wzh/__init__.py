from flask import Flask
from blog import blog


app = Flask(__name__)
app.register_blueprint(blog, url_prefix='/blog')


if __name__ == '__main__':
	app.run(port=5000, debug=True)