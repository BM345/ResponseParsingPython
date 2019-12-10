import xml.etree.ElementTree as ET


class Messages(object):
    def __init__(self):

        self.messages = []

        tree = ET.parse("./rp/messages.en-gb.xml")
        root = tree.getroot()

        for message in root:
            i = message.attrib["id"]
            text = message.text

            self.messages.append({"id": i, "text": text})

    def getMessageById(self, i, p = []):
        text = [message["text"] for message in self.messages if message["id"] == i][0]

        n=0

        for parameter in p:
            n += 1
            tag = "#p{0}#".format(n)
            text = text.replace(tag, str( parameter))

        return text
