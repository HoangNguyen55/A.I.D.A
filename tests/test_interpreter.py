from src.server.interpreter import Lexer


def test_lexer():
    lexer = Lexer()

    assert lexer.scan("Hello World") == ["Hello", "World"]
    assert lexer.scan("'Hello World'") == ["Hello World"]
    assert lexer.scan("search -e google -o html who is amelia watson") == [
        "search",
        "-e",
        "google",
        "-o",
        "html",
        "who",
        "is",
        "amelia",
        "watson",
    ]

    assert lexer.scan('search -e google -o html "who is amelia watson"') == [
        "search",
        "-e",
        "google",
        "-o",
        "html",
        "who is amelia watson",
    ]
