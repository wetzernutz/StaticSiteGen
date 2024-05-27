from typing import override

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None) -> None:
        if tag is None or children is None:
            raise ValueError("Invalid Parent: tag and children are mandatory")
        super().__init__(tag=tag, children=children, props=props)

    @override
    def to_html(self) -> str:
        if len(self.children) == 0:
            raise ValueError("Invalid Parent: children cannot be empty")

        children_html = []
        for child in self.children:
            children_html.append(child.to_html())

        if self.props is not None:
            prop_str = self.props_to_html()
            return f"<{self.tag} {prop_str}>{''.join(children_html)}</{self.tag}>"
        else:
            return f"<{self.tag}>{''.join(children_html)}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.value}), {self.children}, {self.props}"
