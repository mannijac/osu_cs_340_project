from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<p>Hello, Cartridge Collector!</p>"


if __name__ == "__main__":
    app.run(port='9191', host='0.0.0.0')
    
