from App import app
from services import HelloService

@app.route("/", methods=["GET"])
def hello():
    return HelloService.hello()
