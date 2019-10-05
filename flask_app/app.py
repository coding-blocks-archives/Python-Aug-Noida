from flask import Flask

app = Flask("My first application")

@app.route('/')
def index():
  return "hello world !"

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