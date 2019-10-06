#! /usr/bin/python
from flask import Flask, render_template, request, redirect
from scrap import scrap_snapdeal

app = Flask("My first application")

USERS = [
  {
    "name": "Jatin Katyal",
    "language": "Python",
    "state": "Delhi"
  },
  {
    "name": "Ashutosh",
    "language": "JS",
    "state": "Mumbai"
  },
  {
    "name": "Sakshi",
    "language": "C++",
    "state": "Bangalore"
  }
]

FEEDBACKS = []

ABOUT_ME = {
  "name": "Jatin Katyal",
  "languages": [
    "Python",
    "C++",
    "GO"
  ],
  "company": "Coding Blocks"
}

@app.route('/scrap', methods = ['GET', 'POST'])
def scrap():
  if request.method == "POST":
    query = request.form['query']
    result = scrap_snapdeal(query)
    return render_template('scrap.html', result = result)  
  return render_template('scrap.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
  if request.method == 'POST':
    FEEDBACKS.append(request.form)
    # return redirect('/feedbacks')
    return "Thank you for submitting feedback"
  return render_template('form.html')

@app.route('/feedbacks')
def feedbacks():
  return render_template('feedback.html', feedbacks = FEEDBACKS)

@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html', **ABOUT_ME)

# Parameterized URLs
@app.route('/users/<int:id>/<detail>')
def userDetail(id, detail):
  user = USERS[id - 1]
  return user[detail]

@app.route('/users/<int:id>')
def users(id):
  user = USERS[id-1]
  return "Name: {}, Language: {}, State: {}".format(
    user['name'], 
    user['language'], 
    user['state']
  )

@app.route('/')
def index():
  return render_template('index.html', name = "jatin", marks = [1, 2, 3, 4])

@app.route('/languages')
def languages(): 
  return str([
    "java",
    "c++",
    "python",
    "go"
  ])

def main():
  app.run(port=8080, debug=True)

if __name__ == "__main__":
  main()