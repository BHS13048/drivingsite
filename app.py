from flask import Flask, render_template, request
import random, copy
turns = 15
correct = 0
current_question = ""

app = Flask(__name__)

original_questions = {
	'Where is the Taj Mahal?':['Agra','New Delhi','Mumbai','Chennai'],
	'Where is the Great Wall of China?':['China','Beijing','Shanghai','Tianjin'],
	'Where is Petra?':['Ma\'an Governorate','Amman','Zarqa','Jerash'],
	'Where is Machu Picchu?':['Cuzco Region','Lima','Piura','Tacna'],
 	'Where are the Egypt Pyramids?':['Giza','Suez','Luxor','Tanta'],
	'Whrere is the Colosseum?':['Rome','Milan','Bari','Bologna'],
	'Where is Christ the Redeemer?':['Rio de Janeiro','Natal','Olinda','Betim']
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
	global turns
	global current_question
	if turns == 0:
		turns = 15
		return render_template('index.html')
	else:
		turns = turns - 1
		print(turns)
		current_question = random.choice(list(original_questions)) #calls for definition, substitutes q for questions.
		#print(current_question)
		print(current_question)
		for i in questions:
			random.shuffle(questions[i])
		print('gets to this stage')

 #removes the question from the dictionary - currently not working as it also removes the multiple choices
		return render_template('quiz-page.html', q = current_question, o = questions)

@app.route('/quiz_test', methods=['POST'])
def quiz_answers():
	global correct
	for i in questions.keys():
		user_answer = request.form.get("answer")
		if original_questions[i][0] == user_answer:
			correct = correct + 1
	print(correct)
	return quiz()
	#'<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
	app.run(debug=True)