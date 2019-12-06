import nodes

class Marker(object):
    def __init__(self):

        self.position = 0

    def copy(self):
        marker = Marker()

        marker.position = self.position

        return marker

