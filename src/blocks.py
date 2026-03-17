def markdown_to_blocks(markdown):
    # Split by double newlines to find blocks
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        # Strip whitespace and skip empty blocks
        stripped = block.strip()
        if stripped != "":
            filtered_blocks.append(stripped)
    return filtered_blocks
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    # Headings: 1-6 # followed by a space
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BlockType.HEADING

    # Code: Starts and ends with 3 backticks
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE

    # Quote: Every line starts with >
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # Unordered List: Every line starts with "- "
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST

    # Ordered List: Starts with 1. and increments correctly
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.OLIST

    return BlockType.PARAGRAPH
from htmlnode import ParentNode, LeafNode
from markd import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.QUOTE:
        return create_quote_node(block)
    if block_type == BlockType.ULIST:
        return create_ulist_node(block)
    if block_type == BlockType.OLIST:
        return create_olist_node(block)
    if block_type == BlockType.CODE:
        return create_code_node(block)
    if block_type == BlockType.HEADING:
        return create_heading_node(block)
    if block_type == BlockType.PARAGRAPH:
        return create_paragraph_node(block)
    raise ValueError("Invalid block type")

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_ulist_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def create_olist_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        # Split by ". " and take everything after the first period
        text = line[line.find(". ") + 2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def create_code_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found in markdown")
