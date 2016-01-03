#coding:utf8
import sys

class Variables:
    def __init__(self):
        self.items = [0] * 4

    def __getitem__(self, i):
        if i < 0:
            return 0
        if len(self.items) <= i:
            self.items = self.items + [0] * (2*i-len(self.items))
        return self.items[i]

    def __setitem__(self, i, newv):
        if i >= 0:
            if len(self.items) <= i:
                self.items = self.items + [0] * (2*i-len(self.items))
            self.items[i] = newv

    def inc(self, i, delta = 1):
        self[i] += delta

    def dec(self, i, delta = 1):
        self[i] -= delta

    def printall(self):
        print self.items

def Parse(code, debug = False):
    # init
    var = Variables()
    loop = []
    ip = 0
    ptr = 0
    ip_b = len(code)
    while ip < ip_b:
        if code[ip] == '+':
            if ip + 1 < ip_b and code[ip+1] == '(':
                end = code.index(')', ip+2)
                var.inc(ptr, int(code[ip+2:end]))
                ip = end
            else:
                var.inc(ptr)
            if debug:
                print "{}Ptr {} Add To {}".format('\t'*len(loop), ptr, var[ptr])
        elif code[ip] == '-':
            if ip + 1 < ip_b and code[ip+1] == '(':
                end = code.index(')', ip+2)
                var.dec(ptr, int(code[ip+2:end]))
                ip = end
            else:
                var.dec(ptr)
            if debug:
                print "{}Ptr {} Sub To {}".format('\t'*len(loop), ptr, var[ptr])
        elif code[ip] == '>':
            if ip + 1 < ip_b and code[ip+1] == '(':
                end = code.index(')', ip+2)
                ptr += int(code[ip+2:end])
                ip = end
            else:
                ptr += 1
            if debug:
                print "{}Ptr Move To {}".format('\t'*len(loop), ptr)
        elif code[ip] == '<':                     
            if ip + 1 < ip_b and code[ip+1] == '(':
                end = code.index(')', ip+2)
                ptr -= int(code[ip+2:end])
                ip = end
            else:
                ptr -= 1
            if debug:
                print "{}Ptr Move To {}".format('\t'*len(loop), ptr)
        elif code[ip] == '.':
            print chr(var[ptr]),
        elif code[ip] == ',':
            var[ptr] = ord(raw_input())
        elif code[ip] == '[':
            if var[ptr] != 0:
                loop.append((ip, ptr))
            else:
                # skip the loop
                layer = 0
                while ip < ip_b:
                    ip += 1
                    if code[ip] == '[':
                        layer += 1
                    elif code[ip] == ']':
                        layer -= 1
                    if layer == -1:
                        break
            if debug:
                print "{}loop begin at ip: {} ptr: {}".format('\t'*(len(loop)-1), ip, ptr)
        elif code[ip] == ']':
            dest, dummy = loop.pop()
            ip = dest - 1 # Note at the end of the main loop, ip increase itself
            if debug:
                print "{}loop end at ip: {} ptr: {}".format('\t'*len(loop), ip, ptr)
        elif code[ip] == '%':
            while code[ip] != '\n' and ip < ip_b:
                ip += 1
        elif code[ip] == '#':
            if code[ip+1: ip+4] == 'stk':
                print "Stack: ", 
                var.printall()
            elif code[ip+1: ip+4] == 'dbg':
                debug = True
            elif code[ip+1: ip+4] == 'cdb':
                debug = False
        ip += 1

if __name__ == '__main__':
    # start
    code = ""
    if len(sys.argv) < 2:
        while True:
            while True:
                line = sys.stdin.readline().strip('\t')
                if line.strip('\n') == '':
                    print '-----EVALUATION-----'
                    Parse(code, True)
                    code = ''
                    break
                else:
                    code += line
    else:
        code = open(sys.argv[1]).read()
        code = code.strip('\t').strip(' ')
        print '-----EVALUATION-----'
        Parse(code)