from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


responses = []


@app.route('/')
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)


@app.route('/questions/<question_number>')
def questions_pages(question_number):
    """ Generates a page for each question in our survey"""
    question_number_as_number = int(question_number)
    question = satisfaction_survey.questions[question_number_as_number].question
    choices = satisfaction_survey.questions[question_number_as_number].choices

    return render_template(
        "questions.html",
        question_number=question_number_as_number,
        question=question,
        choices=choices)

# Clicking button -> POST request (change some thing in server, redirects) -> immediate getrequest to redirect url ->

@app.route('/questions/<question_number>', methods=['POST'])
def handles_responses(question_number):
    """ Takes in the user's choice and question number and stores answer in response"""
    # print('Made it!')
    # breakpoint()
    answer = request.form["option"]
    # breakpoint()
    responses.append(answer)
    # print(responses)

    question_number = int(question_number) + 1

    return redirect(f'/questions/{question_number}')