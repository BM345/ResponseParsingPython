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
    def __init__(self, messagesFile="./rp/messages.en-gb.xml"):

        self.parser = parsing.Parser()
        self.messages = messages.Messages(messagesFile)

    def validate(self, request):
        if request.expectedResponseType == "integer":
            return self.validateInteger(request)
        if request.expectedResponseType == "nonNegativeInteger":
            return self.validateNonNegativeInteger(request)

        raise ValueError("Unsupported response type '{0}'.".format(request.expectedResponseType))

    def validateInteger(self, request):
        r = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if r != None and r.type == "number" and r.subtype == "integer":
            response.isAccepted = True

            self._applyLeadingZerosConstraints(request, r, response)

            if "mustHaveExplicitSign" not in request.constraints:
                request.constraints["mustHaveExplicitSign"] = False

            if request.constraints["mustHaveExplicitSign"] == True and r.sign == "positive" and r.signIsExplicit == False:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveSign")
            elif request.constraints["mustHaveExplicitSign"] == False and r.sign == "positive" and r.signIsExplicit == True:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("dontHaveSign")

            self._applySignificantFigureConstraints(request, r, response)

        else:
            response.isAccepted = False
            response.messageText = "Your answer should be a whole number."

        response.request = request

        if r != None:
            response.normalisedStudentsResponse = r.asciiMath
            response.expression = r

        return response

    def validateNonNegativeInteger(self, request):
        r = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if r != None and r.type == "number" and r.subtype == "integer" and r.sign == "positive":
            response.isAccepted = True

            self._applyLeadingZerosConstraints(request, r, response)

            if "mustHaveExplicitSign" not in request.constraints:
                request.constraints["mustHaveExplicitSign"] = False

            if request.constraints["mustHaveExplicitSign"] == True and r.signIsExplicit == False:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHavePlusSign")
            elif request.constraints["mustHaveExplicitSign"] == False and r.signIsExplicit == True:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("dontHavePlusSign")

            self._applySignificantFigureConstraints(request, r, response)

        elif r != None and r.type == "number" and r.subtype == "integer" and r.sign == "negative":
            response.isAccepted = False
            response.messageText = "Your answer must be a positive number."

        else:
            response.isAccepted = False
            response.messageText = "Your answer should be a whole number."

        response.request = request

        if r != None:
            response.normalisedStudentsResponse = r.asciiMath
            response.expression = r

        return response

    def _applyLeadingZerosConstraints(self, request, result, response):

        if "allowLeadingZeros" not in request.constraints:
            request.constraints["allowLeadingZeros"] = False

        if request.constraints["allowLeadingZeros"] == False and result.numberOfLeadingZeros > 0 and not result.isZero:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("noLeadingZeros")


    def _applySignificantFigureConstraints(self, request, result, response):

        if "mustHaveAtLeastNSF" in request.constraints:
            n = request.constraints["mustHaveAtLeastNSF"]

            if result.maximumNumberOfSignificantFigures < n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveAtLeastNSF", [n])

        if "mustHaveNoMoreThanNSF" in request.constraints:
            n = request.constraints["mustHaveNoMoreThanNSF"]

            if result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveNoMoreThanNSF", [n])

        if "mustHaveExactlyNSF" in request.constraints:
            n = request.constraints["mustHaveExactlyNSF"]

            if result.maximumNumberOfSignificantFigures < n or result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveExactlyNSF", [n])
