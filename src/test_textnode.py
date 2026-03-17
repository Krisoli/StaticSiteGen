import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()


def test_text_node_to_html_node_text(self):
    node = TextNode("Hello world", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "Hello world")

def test_text_node_to_html_node_link(self):
    node = TextNode("Click me!", TextType.LINK, "https://google.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Click me!")
    self.assertEqual(html_node.props, {"href": "https://google.com"})

def test_text_node_to_html_node_image(self):
    node = TextNode("Alt text", TextType.IMAGE, "https://example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(
        html_node.props,
        {"src": "https://example.com", "alt": "Alt text"},
    )
