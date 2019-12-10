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
        self.expression = None


class Validator(object):
    def __init__(self):

        self.parser = parsing.Parser()
        self.messages = messages.Messages()

    def validate(self, request):
        if request.expectedResponseType == "integer":
            return self.validateInteger(request)

    def validateInteger(self, request):
        r = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if r != None and r.type == "number" and r.subtype == "integer":
            response.isAccepted = True

            if ( "allowLeadingZeros" not in request.constraints or request.constraints["allowLeadingZeros"] == False) and r.numberOfLeadingZeros > 0:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("noLeadingZeros")

            if "mustHaveExplicitSign" in request.constraints:
                if request.constraints["mustHaveExplicitSign"] == True and r.sign == "positive" and r.signIsExplicit == False:
                    response.isAccepted = False
                    response.messageText = self.messages.getMessageById("mustHaveSign")
                elif request.constraints["mustHaveExplicitSign"] == False and r.sign == "positive" and r.signIsExplicit == True:
                    response.isAccepted = False
                    response.messageText = self.messages.getMessageById("dontHaveSign")

        else:
            response.isAccepted = False
            response.messageText = "Your answer should be a whole number."

        response.request = request

        if r != None:
            response.normalisedStudentsResponse = r.asciiMath
            response.expression = r

        return response
