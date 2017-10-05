from flask import Flask, render_template, request
import random, copy
turns = 10
correct = 0
current_question = ""

app = Flask(__name__)

original_questions = {
	'What must you do when red lights are flashing at a railway level crossing?':['Stop unti the lights stop flashing','Check both sides and cross if no trains are coming','Go as soon as the train has passed'],
	'You can park on a dashed yellow line on the side of the road':['True','False'],
	'What must you do when turning right at a roundabout?':['Indicate right as you approach, then left before you exit','Indicate right the whole way around the roundabout','Don\'t indiate right as you approach, but indicate right once on the roundabout','Stay left as you enter the roundabout'],
	'New Zealand\'s road signs are shown in:':['Kilometres per hour','Shown in Miles per hour'],
 	'Who is responsible for making sure passengers below the age of 16 have their seatbelts on?':['Mum','Dad','The driver','Yourself, doesn\'t matter how old you are'],
	'What must you do at a pedestrian crossing?':['Just wait until there are no pedestrians on your side of the crossing','Make sure pedestrians are completely off the road before crossing','Continue, the pedestrians will wait for you'],
	'What must you do if you are looking for something, there is traffic behind you, and travelling well below the speed limit?':['Move to the side to let traffic flow behind you','Continue at the same speed and block traffic flow'],
	'At an uncontrolled intersection, when you are travelling straight you must give way to who?':['Traffic on the right','Traffic on the left','All'],
	'What must you do if you\'re driving and become sleepy?':['Pull over as soon as possible and take a break','Open the window','Speed up to keep up your brain activity'],
	'Can you pass other traffic over a solid yellow line?':['No, that is very dangerous','Yes, if there is 100m of clear space and there is enough space beside to pass without crossing the yellow line','Yellow Lines are the same as white lines']
}

questions = copy.deepcopy(original_questions)
#function shuffles q - questions is later substituted in order to shuffle the questions.



#home page
@app.route('/')
def home_page():
	print('gets to the index page')
	return render_template('index.html')



@app.route('/quiz')
def quiz():
	print('gets here')
	global questions
	global turns
	global current_question
	global correct_answer
	if turns == 0 or questions == {}:
		turns = 10
		correct_answer = ""
		questions = copy.deepcopy(original_questions)
		return render_template('index.html')
	else:
		turns = turns - 1
		print(turns)
		current_question = random.choice(list(original_questions)) 
		print("1" + current_question)
		for i in questions:
			random.shuffle(questions[i])
		return render_template('quiz-page.html', q = current_question, o = questions)



@app.route('/quiz_test', methods=['POST'])
def quiz_answers():
	global correct
	global current_question

	for i in questions.keys():
		user_answer = request.form.get("answer")
		correct_answer = original_questions[i][0]
		if original_questions[i][0] == user_answer:
			correct = correct + 1
	questions.pop(current_question, None)
	return render_template('answer-page.html', a = user_answer, c = correct_answer, q = current_question)
	#'<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'



if __name__ == '__main__':
	app.run(debug=True)