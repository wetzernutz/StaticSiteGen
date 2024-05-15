class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag  
        self.value = value 
        self.children = children
        self.props = props
    
    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> None:
        if (self.props is None or len(self.props)==0):
            return ""
        res = ""
        for k, v in self.props.items():
            res += f"{k}=\"{v}\"" + ' '
        return res.rstrip()

    def __repr__(self) -> str:
        res = ""
        res += f"tag: {self.tag}" + '\n'
        res += f"value: {self.value}" + '\n'
        res += f"children: {self.children}" + '\n'
        res += f"props: {self.props}"
        return res
