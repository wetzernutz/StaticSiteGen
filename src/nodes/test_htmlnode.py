import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        res = node.props_to_html()
        self.assertEqual(res, "href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_empty_props_to_html(self):
        node = HTMLNode(tag="a", props={})
        node2 = HTMLNode(tag="a")
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()