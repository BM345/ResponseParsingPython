import nodes


class Marker(object):
    def __init__(self):

        self.position = 0

    def copy(self):
        marker = Marker()

        marker.position = self.position

        return marker


class ParserSettings(object):
    def __init__(self):

        self.removeLeadingZerosFromSimplifiedForms = False
        self.addLeadingZeroToDecimalsForSimplifiedForms = True


def cut(text, startIndex, length=1):
    a = startIndex
    b = startIndex + length
    return text[a:b]


class Parser(object):
    def __init__(self):

        self.settings = ParserSettings()

    def getParseResult(self, inputText):
        marker = Marker()

        self.parseWhiteSpace(inputText, marker)

        number = self.parseNumber(inputText, marker)

        self.parseWhiteSpace(inputText, marker)

        if number != None and marker.position == len(inputText):
            return number

        return None

    def parseWhiteSpace(self, inputText, marker):
        t = ""
        start = marker.position

        while(marker.position < len(inputText)):
            c = cut(inputText, marker.position)

            if c in " \t\n":
                t += c
                marker.position += 1
            else:
                break

        if len(t) == 0:
            return None

        end = marker.position

        node = nodes.RPWhiteSpaceNode()

        node.start = start
        node.end = end
        node._text = t

        node.value = " "

        node._latex = t
        node._asciiMath = t

        return node

    def parseNumber(self, inputText, marker):
        t = ""
        start = marker.position

        integralPart = ""
        decimalPart = ""

        ts = ""
        sign = "positive"
        signIsExplicit = False

        d = cut(inputText, marker.position)

        if d == "+":
            ts = "+"
            signIsExplicit = True
            marker.position += 1
        elif d == "-":
            ts = "-"
            sign = "negative"
            signIsExplicit = True
            marker.position += 1

        self.parseWhiteSpace(inputText, marker)

        nlz = 0
        ntz = 0
        nsf = 0
        ndp = 0
        
        p = 0
        q = 0

        integralPartIsZero = True    
    
        while marker.position < len(inputText):
            c = cut(inputText, marker.position)

            if c in "0123456789":
                t += c
                marker.position += 1

                if q == 0:
                    integralPart += c
                    if c != "0":
                        integralPartIsZero = False
                else:
                    decimalPart += c
                    ndp += 1

                if c == "0" and nsf == 0 and q == 0:
                    nlz += 1
                elif c != "0":
                    nsf += p
                    p = 0
                    nsf += 1
                elif c == "0" and nsf > 0:
                    p += 1

            elif c == ".":
                if q == 0:
                    t += c
                    marker.position += 1

                    decimalPart += c

                    q += 1
                else:
                    break
            else:
                break

        allZero = True if nsf == 0 and len(t) > 0 else False

        minimumNSF = 0
        maximumNSF = 0

        if allZero:
            minimumNSF = 1
            maximumNSF = 1
            if q > 0:
                ntz = ndp
        else:
            if q > 0:
                minimumNSF = nsf + p
                maximumNSF = nsf + p

                ntz = p
            else:
                minimumNSF = nsf
                maximumNSF = nsf+p

        end = marker.position

        subtype = "integer" if q == 0 else "decimalNumber"

        t1 = ""

        if integralPart == "" and (decimalPart == "" or decimalPart == "."):
            t1 = ""
        elif integralPart == "":
            if self.settings.addLeadingZeroToDecimalsForSimplifiedForms:
                t1 = "0"
            else:
                t1 = ""
        else:
            if self.settings.removeLeadingZerosFromSimplifiedForms:
                t1 = integralPart[nlz:]
                if self.settings.addLeadingZeroToDecimalsForSimplifiedForms:
                    t1 = "0" if t1 == "" else t1
            else:
                t1 = integralPart

        t2 = "" if decimalPart == "." else decimalPart

        if ts + t == "":
            return None
        else:

            node = nodes.RPNumberNode()

            node.subtype = subtype

            node.start = start
            node.end = end
            node._text = ts + t
            node.value = t1 + t2 if allZero else ts + t1 + t2

            node.integralPart = integralPart
            node.decimalPart = decimalPart

            node.sign = sign
            node.signIsExplicit = signIsExplicit
            node.isZero = allZero
            node.integralPartIsZero = integralPartIsZero
            node.numberOfLeadingZeros = nlz
            node.numberOfTrailingZeros = ntz
            node.minimumNumberOfSignificantFigures = minimumNSF
            node.maximumNumberOfSignificantFigures = maximumNSF
            node.numberOfDecimalPlaces = ndp

            return node
