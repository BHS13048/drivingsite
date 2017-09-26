from flask import request
from flask import g
from flask import render_template
from public import website
from public import datamanager

from flask import redirect
from datetime import datetime

#home for driving application

@website.route('/')
def home_page():
    query_string = (
        'SELECT question, answer_one, answer_two, answer_three, answer_four '
        'FROM questions '
    )
    question_no = 1
    query_results = datamanager.query_db(query_string, [], one=False)
    return render_template('index.html', questions=query_results)

@website.route('/quiz-page/<question_no>', methods=['GET', 'POST'])#name that the base-template calls for when the link is clicked
def quiz_page():
    print(request.method)
    if request.method == 'GET':
        query_string = (
            'SELECT question, answer_one, answer_two, answer_three, answer_four '
            'FROM questions '
            'WHERE question_no = ?'
        )
        question_no = '1'
        query_results = datamanager.query_db(query_string, [], one=False)        
        return render_template('quiz-page.html', questions=query_results)
    
    elif request.method == 'POST':
        
        #calls for data entered into the forms by user to be entered into the database
        user_answer = request.form.get('answer') #calls for answer in form
        
        #expected data
        query_string = ( #places variable contents into the database under the correct tables and columns
            'INSERT INTO users( user_answer ) '
            'VALUES (?)'
        )
        query_result = datamanager.query_db(
            query_string,
            [user_answer],
            one=True
        )
        #if user_answer == correct_answer:
        return render_template('quiz-page.html', i=query_result, active='user_answer')
        #else:
            #return render_template('index.html')
    
