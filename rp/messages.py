import xml.etree.ElementTree as ET


class Messages(object):
    def __init__(self, messagesFile="./rp/messages.en-gb.xml"):

        self.messagesFile = messagesFile
        self.messages = []

        tree = ET.parse(messagesFile)
        root = tree.getroot()

        for message in root:
            i = message.attrib["id"]
            text = message.text

            self.messages.append({"id": i, "text": text})

    def getMessageById(self, i, parameters=[]):
        if i not in [message["id"] for message in self.messages]:
            raise ValueError("There is no message with the id '{0}' in {1}.".format(i, self.messagesFile))

        text = [message["text"] for message in self.messages if message["id"] == i][0]

        n = 0

        for parameter in parameters:
            n += 1
            tag = "#p{0}#".format(n)
            text = text.replace(tag, str(parameter))

        return text
