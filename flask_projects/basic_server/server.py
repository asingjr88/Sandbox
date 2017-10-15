from flask import Flask, render_template, request, redirect, session
import os
#flask is base, render allows you to see html, request allows you to pull infomration from forms using dictionary notation, redirect allows you to move to another page automatically, and session allows you to start tracking stuff

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key=os.urandom(32)

@app.route('/')
def index():
  return render_template("test_form.html")
  # this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   # redirects back to the '/' route
   return redirect('/show')
  #redirecting to show so the page will show information taken from form


@app.route('/show')
def show_user():
      return render_template('user.html')
      #return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
    # information being pre-defined during render method
      # return render_template('user.html', name=session['name'], email=session['email'])
    #Form data with request method to add information into session dictionary

app.run(debug=True) # run our server