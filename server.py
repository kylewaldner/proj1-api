from flask import Flask
import os


app = Flask(__name__)


app.config['COUNTER'] = 0


# route
@app.route('/')
# route function
def home():
  # send 'hey!'
  print(app.config['COUNTER'])
  return 'nothing is here'

@app.route('/status')
def status():
  return str(app.config['COUNTER'])


@app.route('/increment')
def increment():
  counter = app.config['COUNTER']
  counter += 1
  app.config['COUNTER'] = counter
  return str(counter)

@app.route('/reset')
def reset():
  app.config['COUNTER'] = 0
  return str(0)

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
