import re
#       Scanner  ->   Evaluator   ->   Parser
# string -^ v- lexemes >-^  v-> tokens >-^ v-> result

def _make_identifiers(string):
    tokens = string.strip().split()
    globals().update({token: token for token in tokens})
    return tokens

TOKENS = _make_identifiers("""
    NUM
    ADD
    SUB
    MUL
    DIV
""")

PATTERNS = [
    (NUM, r"\d+"),
    (ADD, r"[+]"),
    (SUB, r"-"),
    (MUL, r"[×*]"),
    (DIV, r"[÷/]")
    ]


class ParseError(Exception):
    def __init__(self, string, arg):
        self.arg = arg
        self.string = string.format(arg)


class Scanner(object):
    """
    Takes a string of characters and breaks it down to tokens.
    """
    def __init__(self, input_):
        self.input = input_
        self.cur_index = 0

    def ignore_whitespaces(self):
        while self.input[self.cur_index].isspace():
            self.cur_index += 1

    def next_token(self):
        self.ignore_whitespaces()
        token_type, longest = None, ""
        for type_, pattern in PATTERNS:
            match = re.match(pattern, self.input[self.cur_index:])
            if match and match.end() > len(longest):
                token_type, longest = type_, match.group()
        self.cur_index += len(longest)
        if token_type in (ADD, SUB, MUL, DIV):
            return (token_type, None)
        return (token_type, longest)

    def scan(self):
        while len(self.input[self.cur_index:]) > 0:
            yield self.next_token()


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []

    def callback(self, value):
        pass

    def digest_stack(self, token, value):
        pass

    def parse(self):
        for token, value in self.tokens:
            self.digest_stack(token, value)
