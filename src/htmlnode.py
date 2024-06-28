class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""
        if self.props:
            for k in self.props.keys():
                prop_string += f' {k}=\"{self.props[k]}\"'
        return prop_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if (self.value is None) or (self.value == ""):
            raise ValueError("Value is missing")
        if self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if (self.tag is None) or (self.tag == ""):
            raise ValueError("Tag is missing")
        if (self.children is None) or (len(self.children) == 0):
            raise ValueError("Children are missing")
        inner_string=f"<{self.tag}>"
        for node in self.children:
            if type(node) is LeafNode:
                inner_string += f"{node.to_html()}"
            if type(node) is ParentNode:
                inner_string += f"{node.to_html()}"
        return inner_string+f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
