import sys
import logging
import json
from bottle import route, run, template, static_file, request, response

sys.path.append("../rp")

from validation import *

logger = logging.getLogger(__name__)


@route("/api/validate", method="POST")
def api_validate():

    j1 = request.json

    if "studentsResponse" not in j1:
        response.content_type = "application/json"
        return json.dumps({})

    validator = Validator("../rp/messages.en-gb.xml")
    validationRequest = ValidationRequest()

    validationRequest.studentsResponse = j1["studentsResponse"]
    validationRequest.expectedResponseType = j1["expectedResponseType"]
    validationRequest.constraints = j1["constraints"]

    validationResponse = validator.validate(validationRequest)

    response.content_type = "application/json"

    return json.dumps(validationResponse, default=lambda o: o.__dict__)


@route("/<fileName:path>")
def get_static_file(fileName):
    return static_file(fileName, root="")


run(host="localhost", port="8080")
