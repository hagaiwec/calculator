import pyparsing as pp
import operator


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "×": operator.mul,
    "*": operator.mul,
    "÷": operator.truediv,
    "/": operator.truediv
}
expr_stack = []
bnf = None


def push_to_stack(tokens):
    expr_stack.append(tokens[0])


def push_unary_minus(tokens):
    for token in tokens:
        if token == '-':
            expr_stack.append("unary -")


def BNF():
    """
    multop  :: '×' | '÷' | '*' | '/'
    addop   :: '+' | '-'
    real :: ['+' | '-'] '0'..'9'+ [ '.' '0'..'9'* ]
    atom    :: real | '(' expr ')'
    factor  :: atom
    term    :: factor [ multop factor ]*
    expr    :: term [ addop term ]*
    """
    global bnf
    if not bnf:
        # ------- lexical analysis -------
        realnum = pp.Regex(r"[+-]?\d+(?:\.\d*)?")
        plus, minus = map(pp.Literal, "+-")
        mult = pp.Literal("×") | pp.Literal("*")
        div = pp.Literal("÷") | pp.Literal("/")
        lpar, rpar = map(pp.Suppress, "()")

        # ------------ parsing -----------
        expr = pp.Forward()
        addop = plus | minus
        multop = mult | div
        atom = (
            addop[...] + (
                realnum.setParseAction(push_to_stack) |
                pp.Group(lpar + expr + rpar)
                )
            ).setParseAction(push_unary_minus)
        factor = atom
        term = factor + (multop + factor).setParseAction(push_to_stack)[...]
        expr <<= term + (addop + term).setParseAction(push_to_stack)[...]
        bnf = expr
    return bnf


def evaluate_stack(stack):
    op = stack.pop()
    if op == "unary -":
        return -evaluate_stack(stack)
    if op in "+-×*÷/":
        op2 = evaluate_stack(stack)
        op1 = evaluate_stack(stack)
        return OPS[op](op1, op2)
    else:
        # if code got here it means it is an integer.
        try:
            # try to evaluate as int first, if fails then float
            return int(op)
        except ValueError:
            return float(op)


def parse(string):
    BNF().parseString(string, parseAll=True)
    result = evaluate_stack(expr_stack)
    return result