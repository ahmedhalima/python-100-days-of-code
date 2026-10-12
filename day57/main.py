from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home():
    blogs_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blogs_url).json()
    return render_template('index.html', blog_posts = response)

@app.route('/blog/<int:id>')
def read(id):
    posts_url = f'https://api.npoint.io/c790b4d5cab58020d391/{id}'
    response = requests.get(posts_url).json()
    return render_template('post.html', post=response)

if __name__ == '__main__':
    app.run(debug=True)