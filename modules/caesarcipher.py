from base.module import Module
from options import Option
import os.path

__module__ = "Caesarcipher"

class Caesarcipher(Module):
    MODULO=26

    def initialize(self):
        self.update_info({
            'name' : 'Caesar Cipher',
            'description' : 'Caesar cipher decrypter. Just because.',
            'license' : 'BSD',
            'author' : ['rhaps0dy'],
        })
        self.set_options({
            'infile' : Option(True, 'The input file to read the cyphertext from'),
            'outfile' : Option(False, 'The file to write the cleartext to. If it is'+
                        'empty or \'stdout\' the cleartext is printed to screen'),
            'samplesize': Option(False, 'The size of the sample given to choose, in words. Default 10', 10),
        })

    def run(self):
        if not self.samplesize.value is None:
            try:
                self.ssize = int(self.samplesize.value)
            except ValueError:
                self.console.error("'samplesize' must be a either a number or empty.")
                return
        try:
            self.input = open(self.infile.value, 'r')
        except IOError:
            self.console.error("file %s does not exist", self.infile.value)
            return

        if self.outfile.value in [None, 'stdout']:
            self.output = self.console
        elif not os.path.exists(self.outfile.value):
            if not os.path.isfile(self.outfile.value):
                self.console.error("%s already exists and is not a file", self.outfile.value)
                return
            self.console.warning("file %s already exists, do you want to overwrite it? (y/n)", self.outfile.value)
            while True:
                res = self.console.get_input()
                if res.lower() in 'no':
                    return
                elif res.lower() in 'yes':
                    self.output = open(self.outfile.value, 'w')
                    break
                self.console.error("please enter y[es] or n[o].")

        tryline = ""
        wordsofar = 0
        for line in self.input.readlines():
            a = line.split()
            if len(a) < self.ssize-wordsofar:
                wordsofar += self.ssize
                for word in a:
                    tryline += word+" "
            elif len(a)>0:
                for word in a[:(self.ssize-wordsofar-1)]:
                    tryline += word+" "
                print(a)
                tryline+=a[(self.ssize-wordsofar-1)]
                break
        self.console.info("Select the offset of the correct text")
        for offset in range(self.MODULO):
            out = self.performDecryption(tryline, offset)
            self.console.writeln("%d.- %s"%(offset, out))
        offset = 0
        while True:
            try:
                offset = int(self.console.get_input())
                assert 0<=offset
                assert offset < self.MODULO
                break
            except ValueError, AssertionError:
                self.console.error("please enter a number between 0 and %d"%(self.MODULO-1))

        #return file to beginning
        self.input.seek(0)
        for line in self.input.readlines():
            self.output.writeln(self.performDecryption(line, offset).rstrip())

        try:
            self.output.close()
        except AttributeError:
            pass

        self.input.close()

    def performDecryption(self, line, offset):
        out=""
        for c in line:
            if (ord(c) >= ord('a') and ord(c) <= ord('z')):
                out += chr((ord(c)-ord('a')+offset)%self.MODULO + ord('a'))
            elif (ord(c) >= ord('A') and ord(c) <= ord('Z')):
                out += chr((ord(c)-ord('A')+offset)%self.MODULO + ord('A'))
            else:
                out+=c
        return out
