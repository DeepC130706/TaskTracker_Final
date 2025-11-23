from flask import render_template, request, redirect, url_for, jsonify, session
from src.services import task_service, user_service, analytics_service
def register_routes(app):
    @app.route('/')
    def index():
        stats = analytics_service.get_stats()
        return render_template('index.html', stats=stats)

    @app.route('/register', methods=['POST'])
    def register():
        username = request.form.get('username')
        user_service.create_user(username)
        session['user'] = username
        return redirect(url_for('index'))

    @app.route('/tasks', methods=['GET','POST'])
    def tasks():
        if request.method=='POST':
            title = request.form.get('title')
            difficulty = int(request.form.get('difficulty') or 1)
            priority = int(request.form.get('priority') or 1)
            task_service.create_task(title, difficulty, priority)
            return redirect(url_for('tasks'))
        tasks = task_service.list_tasks()
        return render_template('tasks.html', tasks=tasks)

    @app.route('/tasks/<int:task_id>/complete', methods=['POST'])
    def complete(task_id):
        actual_time = float(request.form.get('actual_time') or 0)
        task_service.complete_task(task_id, actual_time)
        return redirect(url_for('tasks'))

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json() or {}
        difficulty = float(data.get('difficulty',1))
        priority = float(data.get('priority',1))
        from src.ml.predictor import Predictor
        pred = Predictor().predict([[difficulty, priority]])[0]
        return jsonify({"predicted_time": float(pred)})
