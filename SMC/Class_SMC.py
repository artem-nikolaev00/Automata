from SMC import AutomataAnalyzer_sm


class Class_SMC:
    def __init__(self):
        self.__counter = 0
        self.__substring = ''
        self.__name = ''
        self.__type = ''
        self._fsm = AutomataAnalyzer_sm.AutomataAnalyzer_sm(self)
        self._is_acceptable = True
        self._fsm.enterStartState()

    def ClearSMC(self):
        self.__substring = ''
        self.CounterZero()
        self.clearSubstring()
        self._is_acceptable = True
        self.__type = ''

    def CheckString(self, string):
        self._fsm.Disk()
        for c in string:
            if not self._is_acceptable:
                break
            if c.isupper() and c.isalpha():
                self._fsm.UpperLiter(c)
            elif c.isalpha():
                self._fsm.Alpha(c)
            elif c.isdigit():
                self._fsm.Digit(c)
            elif c == ':':
                self._fsm.Colon(c)
            elif c == "\\":
                self._fsm.Slash(c)
            elif c == "\n":
                self._fsm.Endl()
            elif c == '.':
                self._fsm.Point(c)
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        if self._is_acceptable:
            return self.__name
        else:
            return None

    def Acceptable(self):
        self._is_acceptable = True

    def Get_type(self):
        return self.__type

    def Unacceptable(self):
        self._is_acceptable = False

    def CounterInc(self):
        self.__counter += 1

    def isValidCounter(self):
        return self.__counter != 0

    def CounterZero(self):
        self.__counter = 0

    def clearSubstring(self):
        self.__substring = ''

    def Add_name(self, c):
        self.__name += c

    def Add_type(self, c):
        self.__type += c

    def Add_str(self, c):
        self.__substring += c

    def isValidName(self):
        return self.__counter <= 31

    def isValidType(self):
        return self.__counter <= 4

    def set_name(self):
        self.__name = self.__substring

    def set_type(self):
        self.__name = self.__type
