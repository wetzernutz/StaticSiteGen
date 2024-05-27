import unittest

from src.nodes.leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_invalid_param_to_html(self):
        with self.assertRaises(ValueError):
            LeafNode("a", None).to_html()

    def test_raw_string_to_html(self):
        node = LeafNode(None, "raw")
        self.assertEqual(node.to_html(), "raw")

    def test_paragraph_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_href_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
