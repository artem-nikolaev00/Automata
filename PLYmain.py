import generator2
import time
from PLY.Parser import Parser
import os


class RecognizerPLY(object):
    input_file = 'input.txt'
    result_file = 'PLY\\result.txt'
    time_file = 'PLY\\time.txt'
    file = False
    stat = dict()

    def __init__(self, flag=False, filename=None):
        self.parser = Parser()
        if flag:
            self.input_file = filename + ".txt"

    def check_from_file(self):
        self.stat.clear()
        f_in = open(self.input_file, 'r')
        f_out = open(self.result_file, 'w')
        f_time = open(self.time_file, 'w')
        f_time.write('time' + '\n')
        n = time.perf_counter()

        for line in f_in.readlines():
            _res = self.parser.Check(line, _file=True)
            if self.parser.flag:
                f_out.write(line.rstrip('\n') + ' - TRUE\n')
            else:
                f_out.write(line.rstrip('\n') + ' - FALSE\n')

        self.stat = self.parser.get_result()

        f_time.write(str(time.perf_counter() - n) + '\n')
        f_time.close()
        print(self.parser.get_j())

    def check_from_console(self, s):
        self.parser.Check(s)
        if self.parser.flag == True:
            print("Good string\n")
        else:
            print("Bad string\n")

    def get_Over(self):
        return self.stat

    def get_Time(self):
        return self.time_file

    def print_result(self):
        print('////////////\n')
        for key, item in self.stat.items():
            print(key + ' - ' + str(item))
        print('////////////\n')

    def save_result(self):
        f = open(os.path.join(os.getcwd(), "PLY\\result.txt"), 'a')
        for key, item in self.stat.items():
            f.write(key + ' - ' + str(item) + '\n')
        f.close()

if __name__ == "__main__":
    print('Press: 1. for reading from file '
          '2. for reading from console')
    n = int(input())

    if n == 1:
        print("Input filename:")
        filename = input()
        generator2.Generator(10000, filename).get_file_content()
        a = RecognizerPLY(True, filename)
        a.check_from_file()
        try:
            f = open(a.get_Time())
            nf = f.read()
            print("Time:", nf.split('\n')[1])
            f.close()
        except IOError as e:
            print("IOError")
        print("Save statistic into file?(yes to show):")
        input_show = input()
        if input_show == "yes":
            a.print_result()
            a.save_result()
            print("saved")
    if n == 2:
        a = RecognizerPLY()
        while True:
            print('Enter the string (to stop write exit)')
            string = input()
            if string != 'exit':
                string += "\n"
                a.check_from_console(s=string)
            else:
                break
    else:
        print("Goodbay. ")