import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_2(self):
        node = HTMLNode("p")
        self.assertEqual(node.props_to_html(), '')

class TestLeafNode(unittest.TestCase):
    def test_leaf_html_1(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(),"<p>This is a paragraph of text.</p>")
    
    def test_leaf_html_2(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_html_3(self):
        leaf = LeafNode(None,"This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "This is a paragraph of text.")

    def test_missing_value_1(self):
        leaf = LeafNode("a", None)
        self.assertRaises(ValueError,leaf.to_html)
    
    def test_missing_value_2(self):
        leaf = LeafNode("a", "")
        self.assertRaises(ValueError,leaf.to_html)

class TestParentNode(unittest.TestCase):
    def test_parent_html_1(self):
        parent = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(parent.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_html_2(self):
        parent = ParentNode("p",[LeafNode("b", "Bold text"),ParentNode("p",[LeafNode("i", "Italic text"),],)],)
        self.assertEqual(parent.to_html(),"<p><b>Bold text</b><p><i>Italic text</i></p></p>")

    def test_missing_tag_1(self):
        parent = ParentNode(None, [LeafNode("b", "Bold text")])
        self.assertRaises(ValueError, parent.to_html)
    
    def test_missing_tag_2(self):
        parent = ParentNode("", [LeafNode("b", "Bold text")])
        self.assertRaises(ValueError, parent.to_html)
    
    def test_missing_children_1(self):
        parent = ParentNode("p", [])
        self.assertRaises(ValueError, parent.to_html)

    def test_missing_children_2(self):
        parent = ParentNode("p", None)
        self.assertRaises(ValueError, parent.to_html)

if __name__ == "__main__":
    unittest.main()
