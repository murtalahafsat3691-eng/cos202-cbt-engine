from flask import Flask, render_template, request, redirect, url_for, session
from models import get_sample_questions
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cos202-secret'

questions = get_sample_questions()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_quiz():
    session.clear()
    session['current_index'] = 0
    session['score'] = 0
    session['answer_stack'] = []
    session['start_time'] = datetime.now().strftime("%d %B %Y at %H:%M")
    return redirect(url_for('question'))

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'current_index' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        answer = request.form.get('answer')
        idx = session['current_index']
        current_q = questions[idx]

        session['answer_stack'].append({
            'question': current_q.text,
            'user_answer': answer,
            'correct': current_q.correct_answer
        })

        if current_q.check_answer(answer):
            session['score'] += 1

        session['current_index'] += 1

        if session['current_index'] >= len(questions):
            return redirect(url_for('results'))
        return redirect(url_for('question'))

    idx = session['current_index']
    current = questions[idx]
    return render_template('quiz.html', question=current, q_num=idx+1, total=len(questions))

@app.route('/results')
def results():
    score = session.get('score', 0)
    total = len(questions)
    percentage = round((score / total) * 100, 1)
    end_time = datetime.now().strftime("%d %B %Y at %H:%M")
    history = session.get('answer_stack', [])

    return render_template('results.html', 
                           score=score, total=total, percentage=percentage,
                           start_time=session.get('start_time'), end_time=end_time,
                           history=history)

if __name__ == '__main__':
    app.run(debug=True)