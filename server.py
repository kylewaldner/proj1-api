from flask import Flask
import os


app = Flask(__name__)

counter = 0

# route
@app.route('/')
# route function
def home():
  # send 'hey!'
  return 'nothing is here'

@app.route('/status')
def status():
  return str(counter)


@app.route('/increment')
def increment():
  counter += 1
  return str(counter)

@app.route('/reset')
def reset():
  counter = 0
  return str(counter)

# listen
if __name__ == "__main__":

  if os.environ['HOME'] == '/home/kyle':
    print("dev mode 1")
    app.run(host='0.0.0.0', port=os.environ['PORT_A']) # 56811
  elif os.environ['FLASK_ENV'] == 'development':
    print("dev mode")
    app.run(host='0.0.0.0', port=5000) # 56811
  else:
    app.run(host='0.0.0.0', port=5000)
  # app.run(port=3000, debug=True)
