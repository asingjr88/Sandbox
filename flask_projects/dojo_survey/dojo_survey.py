from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    print "Let's get moving my friend"
    return render_template('dojo_survey_base.html')

@app.route('/results', methods=["POST"])
def base():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    
    return render_template('dojo_survey_results.html', name=name, location=location, language = language, comment = comment)

# @app.route('/results')
# def results():
#     return render_template('dojo_survey_results.html')

app.run(debug=True)