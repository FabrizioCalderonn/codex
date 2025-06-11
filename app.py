from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

services = []  # simple in-memory list to store services

@app.route('/')
def index():
    return render_template('index.html', services=services)

@app.route('/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        if name and description:
            services.append({'name': name, 'description': description})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
