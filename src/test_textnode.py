import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a text node", "bold", "url")
        self.assertEqual(node, node2)
        self.assertTrue(node==node2)
        
    def test_neq(self):
        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a different text node", "bold", "url")
        self.assertNotEqual(node, node2)
        self.assertFalse(node==node2)

    def test_none_url(self):
        TextNode("text", "bold")
        
if __name__ == "__main__":
    unittest.main()
