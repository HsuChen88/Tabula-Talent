from http import HTTPStatus
from flask import Response, request

from App import app
from services import UserService

@app.route("/user/<id>", methods=["GET"])
def get_user(id: int):
    try:
        user = UserService.get_user(id)
        return user.jsonify()
    except AttributeError:
        return {"message": "no elements found"}, HTTPStatus.BAD_REQUEST
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/user", methods=["POST"])
def create_user():
    try:
        req = request.get_json()
        
        new_user = UserService.create_user(
            req["fullname"], 
            req["email"]
        )
        return new_user.jsonify(), HTTPStatus.CREATED
    except KeyError as err:
        return {"message": "key required not found", "key": err.args[0]}, HTTPStatus.BAD_REQUEST
    except ValueError as err:
        return {"message": err.args[0]}, HTTPStatus.UNPROCESSABLE_ENTITY
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/user/<id>", methods=["PUT"])
def modify_user(id: int):
    try:
        req = request.get_json()
        
        user = UserService.modify_user(
            id,
            req["fullname"], 
            req["email"]
        )
        return user.jsonify()
    except AttributeError:
        return {"message": "no elements found"}, HTTPStatus.BAD_REQUEST
    except KeyError as err:
        return {"message": "Key required not found.", "key": err.args}, HTTPStatus.BAD_REQUEST
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@app.route("/user/<id>", methods=["DELETE"])
def remove_user(id: int):
    try:
        user = UserService.remove_user(id)
        return user.jsonify()
    except AttributeError:
        return {"message": "no elements found"}, HTTPStatus.BAD_REQUEST
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
