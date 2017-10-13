from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') 
def greeting():
    
  print "Now we begin!" 
  return render_template('index.html')
#tried with print and did not work...works with return....test example with print worked
  
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('landing_form.html')

app.run(debug=True)