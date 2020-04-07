

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

    def copyTo(self, node):
        node.supernode = self.supernode
        node.depth = self.depth
        node.type = self.type
        node.subtype = self.subtype
        node.start = self.start
        node.end = self.end
        node._text = self._text
        node._latex = self._latex
        node._asciiMath = self._asciiMath
        node._mathML = self._mathML


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
        self.isZero = False
        self.integralPartIsZero = False
        self.decimalPartIsZero = False
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

    def copyTo(self, node):
        super(RPNumberNode, self).copyTo(node)

        node.value = self.value
        node.integralPart = self.integralPart
        node.decimalPart = self.decimalPart
        node.sign = self.sign
        node.signIsExplicit = self.signIsExplicit
        node.isZero = self.isZero
        node.integralPartIsZero = self.integralPartIsZero
        node.decimalPartIsZero = self.decimalPartIsZero
        node.numberOfLeadingZeros = self.numberOfLeadingZeros
        node.numberOfTrailingZeros = self.numberOfTrailingZeros
        node.minimumNumberOfSignificantFigures = self.minimumNumberOfSignificantFigures
        node.maximumNumberOfSignificantFigures = self.maximumNumberOfSignificantFigures
        node.numberOfDecimalPlaces = self.numberOfDecimalPlaces


class RPCurrencyValueNode(RPNumberNode):
    def __init__(self):
        super(RPCurrencyValueNode, self).__init__()

        self.currency = ""

    @staticmethod
    def fromNumberNode(numberNode):
        currencyValueNode = RPCurrencyValueNode()   

        numberNode.copyTo(currencyValueNode)

        return currencyValueNode

    @RPNode.latex.getter
    def latex(self):
        return self.value

    @RPNode.asciiMath.getter
    def asciiMath(self):
        return self.value
