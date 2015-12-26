#coding:utf8

class Variables:
    def __init__(self):
        self.items = [0] * 4
    def __getitem__(self, i):
        if len(self.items) < i:
            self.items = self.items + [0] * (2*i-len(self.items))
        return self.items[i]
    def __setitem__(self, i, newv):
        if len(self.items) < i:
            self.items = self.items + [0] * (2*i-len(self.items))
        self.items[i] = newv
    def inc(self, i):
        self[i] += 1
    def dec(self, i):
        self[i] -= 1
if __name__ == '__main__':
    # start
    code = raw_input()
    # init
    var = Variables()
    loop = []
    ip = 0
    ptr = 0
    ip_b = len(code)
    while ip < ip_b:
        if code[ip] == '+':
            var.inc(ptr)
        elif code[ip] == '-':
            var.dec(ptr)
        elif code[ip] == '>':
            ptr += 1
        elif code[ip] == '<':
            ptr -= 1
        elif code[ip] == '.':
            print chr(var[ptr])
        elif code[ip] == ',':
            var[ptr] = ord(raw_input())
        elif code[ip] == '[':
            if var[ptr] != 0:
                loop.append(ip)
            else:
                layer = 0
                while ip < ip_b:
                    ip += 1
                    if code[ip] == '[':
                        layer += 1
                    elif code[ip] == ']':
                        layer -= 1
                    if layer == -1:
                        break
        elif code[ip] == ']':
            dest = loop.pop()
            ip = dest - 1 # Note at the end of the main loop, ip increase itself

        ip += 1
