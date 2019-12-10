import xml.etree.ElementTree as ET


class Messages(object):
    def __init__(self):

        self.messages = []

        tree = ET.parse("./rp/messages.en_GB.xml")
        root = tree.getroot()

        for message in root:
            i = message.attrib["id"]
            text = message.text

            self.messages.append({"id": i, "text": text})

    def getMessageById(self, i):
        return [message["text"] for message in self.messages if message["id"] == i][0]
