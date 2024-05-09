from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy data
users = [
    {"name": "Alice", "status": "In Office"},
    {"name": "Bob", "status": "Remote"},
    {"name": "Charlie", "status": "Unavailable"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/api/users')
def api_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
