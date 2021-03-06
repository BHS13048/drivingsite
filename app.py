from flask import Flask, render_template, request
import random, copy

#variables used all over programme
correct = 0
current_question = ""
question_no = 0

#start
app = Flask(__name__)

#question list - first answer in each square bracked is the correct answer, used to check if the user has got each question correct
original_questions = {
	'What must you do when red lights are flashing at a railway level crossing?':['Stop until the lights stop flashing','Check both sides and cross if no trains are coming','Go as soon as the train has passed'],
	'You can park on a dashed yellow line on the side of the road':['False','True'],
	'What must you do when turning right at a roundabout?':['Indicate right as you approach, then left before you exit','Indicate right the whole way around the roundabout','Don\'t indiate right as you approach, but indicate right once on the roundabout','Stay left as you enter the roundabout'],
	'New Zealand\'s road signs are shown in:':['Kilometres per hour','Shown in Miles per hour'],
 	'Who is responsible for making sure passengers below the age of 16 have their seatbelts on?':['The driver','Mum','Dad','Yourself, doesn\'t matter how old you are'],
	'What must you do at a pedestrian crossing with an island?':['Just wait until there are no pedestrians on your side of the crossing','Make sure pedestrians are completely off the road before crossing','Continue, the pedestrians will wait for you'],
	'What must you do if you are looking for something, there is traffic behind you, and travelling well below the speed limit?':['Move to the side to let traffic flow behind you','Continue at the same speed and block traffic flow'],
	'At a roundabout with no give way signs or stop signs on all sides, and you are travelling straight you must give way to who?':['Traffic on the right','Traffic on the left','All'],
	'What must you do if you\'re driving and become sleepy?':['Pull over as soon as possible and take a break','Open the window','Speed up to keep up your brain activity'],
	'Can you pass other traffic over a solid yellow line?':['Yes, if there is 100m of clear space and there is enough space beside to pass without crossing the yellow line','No, that is very dangerous','Yellow Lines are the same as white lines']
}

#temporary question list that resets every tim that 
questions = copy.deepcopy(original_questions)

#home page - page that opens at start, has link to quiz page
@app.route('/')
def home_page():
	global correct, question_no, questions
	correct = 0
	question_no = 0
	questions = copy.deepcopy(original_questions)

#	print('gets to the index page') - used for checking
	return render_template('index.html')

#quiz page - asks user questions, tells the user when and when they don't get the answer correct
@app.route('/quiz')
def quiz():

	#importing global variables as they are used in other definitions as well
	global questions, current_question, current_answer, correct, question_no

	#checks to see how many questions the user is yet to answer, if none then redirect to home and reset
	if question_no == 10 or questions == {}:
		question_no = 0
		correct_answer = ""
		questions = copy.deepcopy(original_questions)
		return render_template('final-answer-page.html', c = correct)
	#if the user still has turns left, take away a turn and carry on
	else:
		question_no = question_no + 1
		#selects randon question from questions
		current_question = random.choice(list(questions)) 
		#print(current_question) - used while checking for bugs
		#shuffle the answers that the user gets to choose from
		for i in questions:
			random.shuffle(questions[i])
		return render_template('quiz-page.html', n = question_no, q = current_question, o = questions)


#
@app.route('/quiz_test', methods=['POST'])
def quiz_answers():
	global correct, current_question, question_no
	#retrieving data from html
	user_answer = request.form.get("answer")
	#checks whether the user got the answer correct by comparing with correct answer from original questions list
	correct_answer = original_questions[current_question][0]
	if correct_answer == user_answer:
		correct = correct + 1
	#lines used for checking if the solution worked
		#print("correct answer")
	#else:
		#print("incorrect answer")
	#removes the current question from the list, original questions list remains the same
		questions.pop(current_question, None)
	#updates every time the user has answered correctly
		print(correct)
	#redirects to the answer page to show the user whether they got the answer correct and what the actual correct answer is
		return render_template('answer-page-correct.html', a = user_answer, c = correct_answer, n = question_no, q = current_question)
	else:
		questions.pop(current_question, None)
		return render_template('answer-page-incorrect.html', a = user_answer, c = correct_answer, n = question_no, q = current_question)
if __name__ == '__main__':
	app.run(debug=True)