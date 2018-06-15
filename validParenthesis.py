out = []
def printValidParenthesis(n):
    open = n/2
    close = n/2
    string = ""
    validParenthesis(open, close, string)
    print(out)


def validParenthesis(open, close, string):
    if open == 0 and close == 0:
        out.append(string)
    if open > close:
        return
    if open > 0:
        validParenthesis(open-1, close, string + "(" )
    if close > 0:
        validParenthesis(open, close-1, string + ")")


printValidParenthesis(8)
