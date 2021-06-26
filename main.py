from flask import Flask, jsonify

app = Flask(__name__)
version = '1.0.0'

@app.route('/')
def main():
  return jsonify({ 'status': 'ok' })

@app.route('/version')
def get_version():
  return jsonify({ 'version': version })

if __name__ == '__main__':
  app.run(port=8080)
