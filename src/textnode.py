class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(tn1, tn2):
        if (tn1.text == tn2.text) and (tn1.text_type == tn2.text_type) and (tn1.url == tn2.url):
            return True
        else:
            return False
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'