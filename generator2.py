from collections import Counter
import string
import random
import os
import time


class Generator:
    def __init__(self, num=1000000, input_file='input.txt'):
        self.num = num
        self.input_file = input_file + ".txt"
        self.result = []
        try:
          self.f = open(self.input_file)
        except IOError as e:
           self.f = open(self.input_file, 'w')
           self.generatefile()

    def randomprob(self):
        return random.random()

    def generatefile(self):
        self.f.close()
        self.f = open(os.path.join(os.getcwd(), self.input_file), 'w')
        n = time.perf_counter()
        for i in range(self.num):
            way = self.disk() + self.colon() + self.way() + self.namef() + self.dot() + self.typ() + '\n'
            self.f.write(way)
        self.f.close()
        n1 = time.perf_counter()
        print('Generate time ')
        print(n1 - n)

    def namef(self, a=0, b=10):  # для каталога 0-1
        letters = random.randint(a, b)
        r = self.randomprob()
        if r < 0.33:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=letters))
        elif r < 0.66:
            return ''.join(random.choices(string.ascii_letters, k=letters))
        else:
            return ''.join(random.choices(string.digits, k=letters))

    def typ(self, a=0, b=10):
        letters = random.randint(a, b)
        r = self.randomprob()
        if self.randomprob() > 0.5:  #########больше процент для каталога
            if r < 0.5:
                return ''.join(random.choices(string.ascii_letters + string.digits, k=letters))
            else:
                k = random.randint(1, 3)
                if k == 1:
                    return 'exe'
                elif k == 2:
                    return 'txt'
                else:
                    return 'png'
        else:
            return ''

    def way(self, a=0, b=20):
        letters = random.randint(a, b)
        st = ''
        ab = ''
        while self.randomprob() < 0.7:
            st = self.catalog(letters)
            ab += st
        return ab

    def catalog(self, letters):
        if self.randomprob() > 0.5:
            return ''.join(random.choices(string.ascii_letters, k=letters)) + '\\'
        else:
            return ''.join(random.choices(string.ascii_letters, k=letters))

    def disk(self):
        r = self.randomprob()
        if r > 0.5:
           return ''.join(random.choice(string.ascii_letters).upper())
        else:
            return ''.join(random.choice(string.ascii_letters))

    def colon(self):
        r = self.randomprob()
        if r < 0.3:
            return ''.join(":\\")
        elif r < 0.6:
            return ''.join(":")
        else:
            return ''

    def dot(self):
        if self.randomprob() > 0.5:  #####больше процент для каталога
            return '.'
        else:
            return ''

    def __del__(self):
        self.f.close()

    def get_num(self):
        return self.__n

    def get_file_content(self):
        try:
            f = open(self.input_file)
        except IOError as e:
            self.generatefile()
            f = open(self.input_file)

        nf = f.read()
        self.result = nf.split('\n')

        f.close()
        return self.result


if __name__ == "__main__":
    gen = Generator()
    A = gen.get_file_content()
    print(A)
