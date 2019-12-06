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
    return text[startIndex, startIndex + length]


class Parser(object):
    def __init__(self):

        self.settings = ParserSettings()

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
