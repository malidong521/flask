from flask import Flask
from config import developmentConfig

app = Flask(__name__)
app.config.from_object(developmentConfig)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()


