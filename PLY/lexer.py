import re
import ply.lex as lex

class Lexer:
    # states = (
    #     ('way', 'exclusive')
    #     ('type', 'exclusive'),
    # )

    tokens = (
        'DISK', 'WAY', 'TYPE',
        'NL', 'UNKNOWN'
    )

    t_ANY_ignore = ''

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_DISK(self, t):
        r'\s*([A-Z]{1})(\:\\)'
        # if t.lexer.current_state() == 'INITIAL':
        #     t.lexer.begin('way')
        # else:
        #     t.lexer.begin('INITIAL')
        return t

    def t_WAY(self, t):
        r'([a-zA-Z0-9]{1,32}\\)*([a-zA-Z0-9]{1,32})(\\{0,1})'
        #t.lexer.begin('type')
        return t

    def t_TYPE(self, t):
        r'(\.[A-Za-z]{1,5})'
        return t

    # def t_type_TYPE(self, t):
    #     r'(\.[A-Za-z]{1,5})'
    #     return t

    def t_ANY_NL(self, t):
        r'\s*(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_UNKNOWN(self, t):
        r'(.)+'
        # print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_error(self, t):
        # print("Illegal character '%s' " % t.value[0])
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t

# data = ''' C:\\\\.r
# '''
#
# a = Lexer()
# a.input(data)
# while True:
#     tok = a.token()
#     if not tok:
#         break
#     print(tok)