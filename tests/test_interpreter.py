import sys, os

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, "..", "src")
sys.path.append(mymodule_dir)

from interpreter import Lexer


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
