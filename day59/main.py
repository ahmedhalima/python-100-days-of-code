import requests
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
@app.route('/')
def home():
    blogs_url = 'https://api.npoint.io/674f5423f73deab1e9a7'
    response = requests.get(blogs_url).json()

    return render_template('index.html', blog_posts = response)

@app.route('/blog/<int:id>')
def read(id):
    newId = id - 1
    posts_url = f'https://api.npoint.io/674f5423f73deab1e9a7/{newId}'
    response = requests.get(posts_url).json()
    return render_template('post.html', post=response)


@app.route('/about')
def about():
    return render_template('about.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.post('/contact')
def contactPost():
    username = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    flash('You contact message has been received.', 'success')
    return redirect(request.referrer)
    return username

if __name__ == '__main__':
    app.run(debug=True)