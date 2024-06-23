import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_2(self):
        node = HTMLNode("p")
        self.assertEqual(node.props_to_html(), '')


if __name__ == "__main__":
    unittest.main()
