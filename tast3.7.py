from xml.etree.ElementTree import XMLParser
import sys


class MaxDepth:  # The target object of the parser
    depth = 0
    sizes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        self.sizes[attrib['color']] += self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return self.sizes


target = MaxDepth()
parser = XMLParser(target=target)
parser.feed(input())
values = parser.close()
print('{} {} {}'.format(values['red'], values['green'], values['blue']))
