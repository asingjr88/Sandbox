from flask import Flask, session, redirect, request, render_template
from datetime import datetime
import os 
import random  

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def start():
    print('Hello Moto')
    if 'gold' not in session:
        session['gold']=100
        session['updates']=[]
        return render_template("ninja_gold.html", gold=session['gold'], updates=session['updates'])

@app.route('/process_money', methods=['POST'])
def process():
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    building= request.form['building']
    if building == 'farm':
        gold = random.randrange(10,21)
        session['updates'].append({'update':"You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})      
    elif building == 'cave':
        gold = random.randrange(5,11)
        session['updates'].append({'update': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})
    elif building == 'house':
        gold = random.randrange(2,6)
        session['updates'].append({'update': "You entered a {} and earned    {} golds".format(building, gold), 'class':'win', 'date':time})
    else: 
        building == 'casino'
        gold = random.randrange(-50,51)
        if gold < 0:
            session['updates'].append({'update': "You entered a {} and       lost {} golds".format(building, gold), 'class': 'loss',          'date':time})
        else:
            session['updates'].append({'update': "You entered a {} and       earned {} golds".format(building, gold), 'class':'win',     'date':time})
          
    session['gold'] += gold
    return redirect('/')

app.run(debug=True)

