from flask import Flask
import os


app = Flask(__name__)

# route
@app.route('/')
# route function
def home():
  # send 'hey!'
  return 'nothing is here'


@app.route('/fire')
def fire():
  return 'yes'

# listen
if __name__ == "__main__":

  if os.environ['HOME'] == '/home/kyle':
    print("dev mode 1")
    app.run(host='0.0.0.0', port=os.environ['PORT_A']) # 56811
  elif os.environ['FLASK_ENV'] == 'development':
    print("dev mode")
    app.run(host='0.0.0.0', port=os.environ['PORT_A']) # 56811
  else:
    app.run(host='0.0.0.0', port=5000)
  # app.run(port=3000, debug=True)
