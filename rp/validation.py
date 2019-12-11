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
        result = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if request.expectedResponseType == "integer":
            self.validateInteger(request, result, response)
        elif request.expectedResponseType == "nonNegativeInteger":
            self.validateNonNegativeInteger(request, result, response)
        else:
            raise ValueError("Unsupported response type '{0}'.".format(request.expectedResponseType))

        response.request = request

        if result != None:
            response.normalisedStudentsResponse = result.asciiMath
            response.expression = result

        return response

    def validateInteger(self, request, result, response):
        response.isAccepted = True

        if result == None:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleInteger")
            return

        if result.type != "number":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleInteger")
            return

        if result.subtype != "integer":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeInteger")
            return

        self._applyLeadingZerosConstraints(request, result, response)

        if response.isAccepted == False:
            return

        if "mustHaveExplicitSign" not in request.constraints:
            request.constraints["mustHaveExplicitSign"] = False

        if request.constraints["mustHaveExplicitSign"] == True and result.sign == "positive" and result.signIsExplicit == False:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustHaveSign")
            return

        if request.constraints["mustHaveExplicitSign"] == False and result.sign == "positive" and result.signIsExplicit == True:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("dontHaveSign")
            return

        self._applySignificantFigureConstraints(request, result, response)

    def validateNonNegativeInteger(self, request, result, response):
        response.isAccepted = True

        if result == None:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleInteger")
            return

        if result.type != "number":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleInteger")
            return

        if result.subtype != "integer":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeInteger")
            return

        if result.sign == "negative":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBePositive")
            return

        self._applyLeadingZerosConstraints(request, result, response)

        if response.isAccepted == False:
            return

        if "mustHaveExplicitSign" not in request.constraints:
            request.constraints["mustHaveExplicitSign"] = False

        if request.constraints["mustHaveExplicitSign"] == True and result.signIsExplicit == False:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustHavePlusSign")
            return

        if request.constraints["mustHaveExplicitSign"] == False and result.signIsExplicit == True:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("dontHavePlusSign")
            return

        self._applySignificantFigureConstraints(request, result, response)

    def _applyLeadingZerosConstraints(self, request, result, response):

        if "allowLeadingZeros" not in request.constraints:
            request.constraints["allowLeadingZeros"] = False

        if request.constraints["allowLeadingZeros"] == False and result.numberOfLeadingZeros > 0 and not result.isZero:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("noLeadingZeros")
            return

    def _applySignificantFigureConstraints(self, request, result, response):

        if "mustHaveAtLeastNSF" in request.constraints:
            n = request.constraints["mustHaveAtLeastNSF"]

            if result.maximumNumberOfSignificantFigures < n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveAtLeastNSF", [n])
                return

        if "mustHaveNoMoreThanNSF" in request.constraints:
            n = request.constraints["mustHaveNoMoreThanNSF"]

            if result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveNoMoreThanNSF", [n])
                return

        if "mustHaveExactlyNSF" in request.constraints:
            n = request.constraints["mustHaveExactlyNSF"]

            if result.maximumNumberOfSignificantFigures < n or result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("mustHaveExactlyNSF", [n])
                return
