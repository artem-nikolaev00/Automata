import os
import generator2
import re
import time


class Myclass:
    stat = dict()
    result_file = 'Regular\\result.txt'
    time_file = 'Regular\\time.txt'
    input_file = 'input.txt'
    file = False

    def __init__(self, flag=False, strings=None):
        self.file = flag
        if flag:
            self.f = open(self.result_file, 'w')
            self.strings = strings

    def __del__(self):
        if self.file:
            self.f.close()

    def check_from_file(self):
        self.stat.clear()
        f_time = open(self.time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.time_file, 'a')
        n = time.perf_counter()
        j = 0
        for i in range(len(self.strings) - 1):
            match = re.fullmatch(r'^(([A-Z]{1})(\:\\)|'
                                 r'([A-Z]{1})(\:\\)(([a-zA-Z0-9]{1,32}\\)*([a-zA-Z0-9]{1,32})|([a-zA-Z0-9]{1,32}\\)*(['
                                 r'a-zA-Z0-9]{1,32})(\.[A-Za-z]{1,5}))(\s*)|'
                                 r'([A-Z]{1})(\:\\)(([a-zA-Z0-9]{1,32}\\)*(\.[A-Za-z]{1,5})*)(\s*))$', self.strings[i])
            if match is not None:
                j += 1
                a = match[11]
                b = match[17]
                if a:
                    self.result(a)
                elif b:
                    self.result(b)
                else:
                    self.result('catalog')
                self.strings[i] += ' - TRUE' + '\n'
                self.f.write(self.strings[i])
            else:
                self.strings[i] += ' - FALSE' + '\n'
                self.f.write(self.strings[i])
        f_time.write(str(time.perf_counter() - n) + '\n')
        f_time.close()
        print("Count of '-TRUE':")
        print(j)

    def check_from_console(self, s):
        match = re.fullmatch(r'^(([A-Z]{1})(\:\\)|'
                             r'([A-Z]{1})(\:\\)(([a-zA-Z0-9]{1,32}\\)*([a-zA-Z0-9]{1,32})|([a-zA-Z0-9]{1,32}\\)*(['
                             r'a-zA-Z0-9]{1,32})(\.[A-Za-z]{1,5}))(\s*)|'
                             r'([A-Z]{1})(\:\\)(([a-zA-Z0-9]{1,32}\\)*(\.[A-Za-z]{1,5})*)(\s*))$', s)
        if match is not None:
            print('Good string\n')
        else:
            print('Bad string\n')

    def result(self, key):
        if self.stat.get(key) is None:
            self.stat[key] = 1
        else:
            num = self.stat.get(key)
            self.stat[key] = num + 1

    def print_result(self):
        print('////////////\n')
        for key, item in self.stat.items():
            print(key + ' - ' + str(item))
        print('////////////\n')

    def save_result(self):
        f = open(os.path.join(os.getcwd(), "Regular\\result.txt"), 'a')
        for key, item in self.stat.items():
            f.write(key + ' - ' + str(item) + '\n')
        self.f.close()

    def get_Time(self):
        return self.time_file

if __name__ == "__main__":
    print('Press: 1. for reading from file '
          '2. for reading from console')
    n = int(input())

    if n == 1:
        print("Input filename:")
        filename = input()
        all_strings = generator2.Generator(1000000, filename).get_file_content()
        a = Myclass(True, all_strings)
        a.check_from_file()
        try:
            f = open(a.get_Time())
            nf = f.read()
            print("Time:", nf.split('\n')[1])
            f.close()
        except IOError as e:
            print("---- Error ----")
        print("Save statistic into file?(yes to show):")
        input_show = input()
        if input_show == "yes":
            a.print_result()
            a.save_result()
            print("Data saved to files")
    if n == 2:
        string = ''
        a = Myclass('')
        while True:
            print('Enter the string (to stop write exit)')
            string = input()
            if string != 'exit':
                a.check_from_console(s=string)
            else:
                break
    else:
        print("Goodbay. ")

