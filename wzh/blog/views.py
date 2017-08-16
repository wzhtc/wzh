from flask import request, render_template, redirect, url_for
from . import blog

@blog.route('/')
def home():
    return redirect(url_for('.index'))

@blog.route('/index')
def index():
	return render_template('index.html')


@blog.route('/post')
def post():
	return render_template('post.html')


@blog.route('/about')
def about():
	return render_template('about.html')



@blog.route('/contact')
def contact():
	return render_template('contact.html')