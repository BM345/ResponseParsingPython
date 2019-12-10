import parsing
import messages


class ValidationRequest(object):
    def __init__(self):

        self.studentsResponse = ""
        self.expectedResponseType = ""
        self.constraints = {}
        self.localisationSettings = {}


class ValidationResponse(object):
    def __init__(self):

        self.isAccepted = True
        self.messageText = ""
        self.request = None
        self.normalisedStudentsResponse = ""
        self.expressionTree = None


class Validator(object):
    def __init__(self):

        self.parser = parsing.Parser()
        self.messages = messages.Messages()

    def validate(self, request):
        if request.expectedResponseType == "integer":
            return self.validateInteger(request)

    def validateInteger(self,  request):
        r = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if r != None and r.type == "number" and r.subtype == "integer":
            response.isAccepted = True

            if "allowLeadingZeros" in request.constraints:
                if request.constraints["allowLeadingZeros"] == False and r.numberOfLeadingZeros > 0:
                    response.isAccepted = False
                    response.messageText = self.messages.getMessageById("noLeadingZeros")
        else:
            response.isAccepted = False
            response.messageText = "Your answer should be a whole number."

        response.request = request

        if r != None:
            response.normalisedStudentsResponse = r.asciiMath
            response.expressionTree = r

        return response
