from textnode import TextNode


def main():
    text, text_type, url = "This is a Text Node", "bold", "https://www.boot.dev"
    node = TextNode(text, text_type, url)
    print(node)


if __name__ == '__main__':
    main()