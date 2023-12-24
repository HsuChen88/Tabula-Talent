# local library
from ..app import app
from ..services import hello_service

@app.route("/", methods=["GET"])
def hello():
    return hello_service.hello()
