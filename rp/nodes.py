

class RPNode(object):
    def __init__(self, nodeType):
        self.supernode = None
        self.depth = 0

        self.type = nodeType
        self.subtype = ""

        self.start = 0
        self.end = 0
        self._text = ""

        self._latex = ""
        self._asciiMath = ""
        self._mathML = ""

    @property
    def length(self):
        return self.end - self.start

    @property
    def text(self):
        return self._text

    @property
    def latex(self):
        return self._latex

    @property
    def asciiMath(self):
        return self._asciiMath

    @property
    def mathML(self):
        return self._mathML

    @property
    def subnodes(self):
        return []

    @subnodes.setter
    def subnodes(self, value):
        pass

    def setDepth(self, depth=0):
        self.depth = depth

        for node in self.subnodes:
            node.supernode = self
            node.setDepth(depth + 1)


class RPWhiteSpaceNode(RPNode):
    def __init__(self):
        super(RPWhiteSpaceNode, self).__init__("whiteSpace")

        self.value = ""


class RPNumberNode(RPNode):
    def __init__(self):
        super(RPNumberNode, self).__init__("number")

        self.value = ""
        self.integralPart = ""
        self.decimalPart = ""
        self.sign = ""
        self.signIsExplicit = False
        self.numberOfLeadingZeros = 0
        self.numberOfTrailingZeros = 0
        self.minimumNumberOfSignificantFigures = 0
        self.maximumNumberOfSignificantFigures = 0
        self.numberOfDecimalPlaces = 0

    @RPNode.latex.getter
    def latex(self):
        return self.value

    @RPNode.asciiMath.getter
    def asciiMath(self):
        return self.value
