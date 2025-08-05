from flask import Flask, render_template, redirect, url_for
from redis_client import r
from db import init_db, update_vote

app = Flask(__name__)

animals = ['elephant', 'lion', 'cat', 'dog']

@app.route('/')
def index():
    votes = {animal: int(r.get(f'vote:{animal}') or 0) for animal in animals}
    return render_template('index.html', animals=animals, votes=votes)

@app.route('/vote/<animal>', methods=['POST'])
def vote(animal):
    if animal in animals:
        r.incr(f'vote:{animal}')
        count = int(r.get(f'vote:{animal}'))
        update_vote(animal, count)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

