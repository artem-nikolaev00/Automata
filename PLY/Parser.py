from PLY import lexer
import ply.yacc as yacc
import os

class Parser:

    tokens = lexer.Lexer.tokens

    def __init__(self):
        self.lexer = lexer.Lexer()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._result = {}
        self.flag = False
        self.j = 0

    def p_string(self, p):
        """string : DISK WAY TYPE NL
        | DISK WAY NL
        | DISK NL
        | DISK TYPE NL"""
        if len(p) == 5:
            p[0] = p[1] + p[2] + p[3] + p[4]
            self.result(p[3])
        if len(p) == 4:
            p[0] = p[1] + p[2] + p[3]
            if p[2][0] == ".":
                self.result(p[2])
            else:
                self.result('catalog')
        if len(p) == 3:
            p[0] = p[1] + p[2]
            self.result('catalog')
        self.flag = True
        if self.flag == True:
            self.j += 1

    def get_j(self):
        return self.j

    def result(self, key):
        if self._result.get(key) is None:
            self._result[key] = 1
        else:
            num = self._result.get(key)
            self._result[key] = num + 1

    def get_result(self):
        return self._result

    def p_string_zero_error(self, p):
        """string : err NL"""
        p[0] = p[1] + p[2]

    def p_string_first_error(self, p):
        """string : DISK err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_string_second_error(self, p):
        """string : DISK WAY err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]

    def p_error(self, p):
        pass

    def Check(self, s, f=False):
        if f == False:
            self._result.clear()
        self.flag = False
        _res = self.parser.parse(s)
        return s

# string = '''C:\\ddvsdv\\.r
# '''
# y = Parser()
# y.Check(string)
# print(y.flag)