from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_env_string():
    env_string = os.environ.get('MESSAGE', 'Значение не установлено!')
    return f'{env_string}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)