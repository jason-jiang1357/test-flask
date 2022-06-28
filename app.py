from flask import Flask

app = Flask("__name__")

@route("/")
def index():
    return "docker container >> flask >> hello"
    
if __name__ == "__main__":
    app.run()