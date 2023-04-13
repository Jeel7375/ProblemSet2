from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
            print(data)

infile = open('C:/Users/briju/Desktop/DP/ProblemSet2/w3c.txt')
content = infile.read()
infile.close()
hp = MyHTMLParser()
hp.feed(content)