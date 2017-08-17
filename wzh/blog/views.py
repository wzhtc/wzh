import markdown
from flask import request, render_template, redirect, url_for, Markup
from . import blog
import requests
from .models import Post


@blog.route('/')
def home():
    return redirect(url_for('.index'))

@blog.route('/index')
def index():
	posts = [post for post in Post.objects]
	content = {'objects':posts}
	return render_template('index.html', **locals())


@blog.route("/post/<fileid>")
def post(fileid):
    print(fileid)
    page = download_file_from_google_drive(fileid)
    page = Markup(markdown.markdown(page))
    return render_template('post.html', **locals())


@blog.route('/about')
def about():
	return render_template('about.html')



@blog.route('/contact')
def contact():
	return render_template('contact.html')



def download_file_from_google_drive(id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    return save_response_content(response)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response):
    CHUNK_SIZE = 32768    
    return ''.join([chunk.decode('utf-8') for chunk in response.iter_content(CHUNK_SIZE)])
