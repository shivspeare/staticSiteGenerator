import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_2(self):
        node = HTMLNode("p")
        self.assertEqual(node.props_to_html(), '')

class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(),"<p>This is a paragraph of text.</p>")
    
    def test_to_html_2(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_3(self):
        leaf = LeafNode(None,"This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "This is a paragraph of text.")


if __name__ == "__main__":
    unittest.main()
