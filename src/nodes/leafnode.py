from typing import override
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    @override
    def to_html(self) -> None:
        if (self.value is None):
            raise ValueError("Invalid HTML, no value")
        if (self.tag is None):
            return self.value
        if (self.props is not None):
            prop_str = self.props_to_html()
            return f"<{self.tag} {prop_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}), {self.props}"
        
