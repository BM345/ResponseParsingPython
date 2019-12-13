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
        self.messages = messages.Messages(messagesFile )

        self.integerAllowedCharacters = "0123456789+- "
        self.nonNegativeIntegerAllowedCharacters = "0123456789+ "
        self.decimalAllowedCharacters = "0123456789.+- "

    def validate(self, request):
        result = self.parser.getParseResult(request.studentsResponse)

        response = ValidationResponse()

        if request.expectedResponseType == "integer":
            self.validateInteger(request, result, response)
        elif request.expectedResponseType == "nonNegativeInteger":
            self.validateNonNegativeInteger(request, result, response)
        elif request.expectedResponseType == "decimal":
            self.validateDecimal(request, result, response)
        elif request.expectedResponseType == "currencyValue":
            self.validateCurrencyValue(request, result, response)
        else:
            raise ValueError("Unsupported response type '{0}'.".format(request.expectedResponseType))

        response.request = request

        if result != None:
            response.normalisedStudentsResponse = result.asciiMath
            response.expression = result

        return response

    def validateInteger(self, request, result, response):
        response.isAccepted = True

        for c in request.studentsResponse:
            if c not in self.integerAllowedCharacters:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("onlyUseIntegerCharacters")
                return

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

        for c in request.studentsResponse:
            if c not in self.nonNegativeIntegerAllowedCharacters:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("onlyUseNonNegativeIntegerCharacters")
                return

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

    def validateDecimal(self, request, result, response):
        response.isAccepted = True

        for c in request.studentsResponse:
            if c not in self.decimalAllowedCharacters:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("onlyUseDecimalCharacters")
                return

        if result == None or result.type != "number":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleNumber")
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

        if response.isAccepted == False:
            return

        self._applyDecimalPlaceConstraints(request, result, response)

        if response.isAccepted == False:
            return

    def validateCurrencyValue(self, request, result, response):
        response.isAccepted = True

        for c in request.studentsResponse:
            if c not in self.decimalAllowedCharacters:
                response.isAccepted = False
                response.messageText = self.messages.getMessageById("onlyUseDecimalCharacters")
                return

        if result == None or result.type != "number":
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustBeSingleNumber")
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

        if not (request.constraints["currency"] == "USD" or request.constraints["currency"] == "GBP"):
            return

        if result.numberOfDecimalPlaces != 0 and result.numberOfDecimalPlaces != 2:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("mustHaveExactlyNDP", [2])
            return

    def _applyLeadingZerosConstraints(self, request, result, response):

        if "allowLeadingZeros" not in request.constraints:
            request.constraints["allowLeadingZeros"] = False

        n = 1 if result.integralPartIsZero else 0

        if request.constraints["allowLeadingZeros"] == False and result.numberOfLeadingZeros > n:
            response.isAccepted = False
            response.messageText = self.messages.getMessageById("noLeadingZeros")
            return

    def _applySignificantFigureConstraints(self, request, result, response):

        if "mustHaveAtLeastNSF" in request.constraints:
            n = request.constraints["mustHaveAtLeastNSF"]

            if result.maximumNumberOfSignificantFigures < n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveAtLeast1SF")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveAtLeastNSF", [n])
                return

        if "mustHaveNoMoreThanNSF" in request.constraints:
            n = request.constraints["mustHaveNoMoreThanNSF"]

            if result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveNoMoreThan1SF")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveNoMoreThanNSF", [n])
                return

        if "mustHaveExactlyNSF" in request.constraints:
            n = request.constraints["mustHaveExactlyNSF"]

            if result.maximumNumberOfSignificantFigures < n or result.minimumNumberOfSignificantFigures > n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveExactly1SF")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveExactlyNSF", [n])
                return

    def _applyDecimalPlaceConstraints(self, request, result, response):

        if "mustHaveAtLeastNDP" in request.constraints:
            n = request.constraints["mustHaveAtLeastNDP"]

            if result.numberOfDecimalPlaces < n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveAtLeast1DP")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveAtLeastNDP", [n])
                return

        if "mustHaveNoMoreThanNDP" in request.constraints:
            n = request.constraints["mustHaveNoMoreThanNDP"]

            if result.numberOfDecimalPlaces > n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveNoMoreThan1DP")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveNoMoreThanNDP", [n])
                return

        if "mustHaveExactlyNDP" in request.constraints:
            n = request.constraints["mustHaveExactlyNDP"]

            if result.numberOfDecimalPlaces != n:
                response.isAccepted = False
                if n == 1:
                    response.messageText = self.messages.getMessageById("mustHaveExactly1DP")
                else:
                    response.messageText = self.messages.getMessageById("mustHaveExactlyNDP", [n])
                return
