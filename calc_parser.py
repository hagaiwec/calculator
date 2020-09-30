import pyparsing as pp
import operator


expr_stack = []
bnf = None


def push_to_stack(tokens):
    expr_stack.append(tokens[0])


def push_unary_minus(tokens):
    if tokens[0] == "-":
        expr_stack.append("unary -")


def BNF():
    """
    multop  :: '×' | '÷' | '*' | '/'
    addop   :: '+' | '-'
    integer :: ['+' | '-'] '0'..'9'+
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
        mult = pp.oneOf("×*")
        div = pp.oneOf("÷/")
        lpar, rpar = map(pp.Supress, "()")

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
