class Lexer:
    """
    A class to scan the input string and seperate it into chunks called tokens
    """

    def __init__(self) -> None:
        self._tokens: list[str] = []
        self._input: str = ""
        self._position = -1

    def _is_at_end(self):
        return self._position >= len(self._input)

    def _get_next_char(self) -> str:
        self._position += 1
        if self._position >= len(self._input):
            return ""

        return self._input[self._position]

    def _match(self, match_char: str) -> str:
        token = ""
        while not self._is_at_end():
            char = self._get_next_char()
            if char is not match_char:
                token += char
            else:
                break

        return token

    def scan(self, input: str) -> list[str]:
        """
        Turn an input string to list of tokens
        """
        self._input: str = input
        self._position = -1
        tokens: list[str] = []

        while not self._is_at_end():
            char = self._get_next_char()
            match char:
                # treat everything inside quote as a single token
                case '"':
                    tokens.append(self._match('"'))
                case "'":
                    tokens.append(self._match("'"))

                # ignore white spaces
                case "":
                    pass
                case " ":
                    pass
                case "\t":
                    pass

                # if its any other char, its likely a word
                case _:
                    tokens.append(char + self._match(" "))

        return tokens


class AidaInterpreter:
    def __init__(self) -> None:
        pass
