from pygments import highlight
from pygments import lexers
from pygments.formatters import HtmlFormatter

def showcode(content, syntax):
    lex = lexers.get_lexer_by_name(syntax,  stripall=True)
    formatter = HtmlFormatter(linenos=True, noclasses=True, full = True)
    return highlight(content, lex, formatter)
    
