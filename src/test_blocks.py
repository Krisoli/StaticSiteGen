import unittest
from blocks import markdown_to_blocks

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph",
            ],
        )

if __name__ == "__main__":
    unittest.main()
def test_block_to_block_types(self):
    self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
    self.assertEqual(block_to_block_type("> quote\n> more quote"), BlockType.QUOTE)
    self.assertEqual(block_to_block_type("- list\n- items"), BlockType.ULIST)
    self.assertEqual(block_to_block_type("1. first\n2. second"), BlockType.OLIST)
    self.assertEqual(block_to_block_type("just a paragraph"), BlockType.PARAGRAPH)

def test_block_to_block_type_ordered_list_fail(self):
    # Should be paragraph because the numbering is broken (1, 2, 4)
    block = "1. first\n2. second\n4. fourth"
    self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
def test_markdown_to_html_node(self):
    md = """
# Heading

This is a paragraph.

- item 1
- item 2
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertIn("<h1>Heading</h1>", html)
    self.assertIn("<p>This is a paragraph.</p>", html)
    self.assertIn("<ul><li>item 1</li><li>item 2</li></ul>", html)
