from base.module import Module
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
            'infile' : [True, 'The input file to read the cyphertext from'],
            'outfile' : [False, 'The file to write the cleartext to. If it is'+
                        'empty or \'stdout\' the cleartext is printed to screen'],
            'samplesize': [False, 'The size of the sample given to choose, in words. Default 10', 1],
        })

    def run(self):
        if not self.samplesize.get() is None:
            try:
                self.ssize = int(self.samplesize.get())
            except ValueError:
                self.console.error("'samplesize' must be a either a number or empty.")
                return
        try:
            self.input = open(self.infile.get(), 'r')
        except IOError:
            self.console.error("file %s does not exist", self.infile.get())
            return

        if self.outfile.get() in [None, 'stdout']:
            self.output = self.console
        elif not os.path.exists(self.outfile.get()):
            if not os.path.isfile(self.outfile.get()):
                self.console.error("%s already exists and is not a file", self.outfile.get())
                return
            self.console.warning("file %s already exists, do you want to overwrite it? (y/n)", self.outfile.get())
            while True:
                res = self.console.get_input()
                if res.lower() in 'no':
                    return
                elif res.lower() in 'yes':
                    self.output = open(self.outfile.get(), 'w')
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
