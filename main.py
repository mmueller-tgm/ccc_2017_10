#!/usr/bin/python3.5
import re


class main:
    def __init__(self, file):
        # {"acc_num": (name, amt, limit)}
        self.acc = {}
        # {"time": (from, to, amount)}
        self.trans = {}
        self.file = file
        self.reader()
        timestamps = sorted(self.trans.keys())
        for i in timestamps:
            self.submit_transaction(i)

        self.output()


    def submit_transaction(self, tid):
        src = self.trans[tid][0]
        dest = self.trans[tid][1]
        amt = int(self.trans[tid][2])
        if self.acc[src][1] - amt >= (-self.acc[src][2]):
            self.acc[dest][1] += amt
            self.acc[src][1] -= amt

    def output(self):
        file = open(self.file+"_out", "w")
        file.write("%i\n"%self.acc_num)
        for (i, j) in self.acc.items():
            file.write("%s %s\n"%(j[0], j[1]))
        print(self.acc)

    @staticmethod
    def check_if_valid(aid):
        if re.search('CAT*\d\d\w{10}', aid):
            valid = True
            for char in ''.join([c for c in aid[3:] if c.isupper()]):
                if char.lower() not in aid[3:]:
                    valid = False
            if valid:
                return True
        return False

    def reader(self):
        print("reading"+self.file)
        read = open(self.file)
        self.acc_num = int(read.readline())
        self.acc = {}
        for i in range(0, self.acc_num):
            j = read.readline().replace("\n", "")
            j = j.split(" ")
            if self.check_if_valid(j[1]):
                self.acc[j[1]]=[j[0], int(j[2]), int(j[3])]
        self.acc_num = len(self.acc)

        self.trans_num = int(read.readline())
        self.trans = {}
        for i in range(0, self.trans_num):
            j = read.readline().replace("\n", "")
            j = j.split(" ")
            if self.check_if_valid(j[0]) and self.check_if_valid(j[1]):
                self.trans[j[3]]=(j[0], j[1], j[2])
        self.trans_num = len(self.trans)



if __name__ == "__main__":
    main("L2/level2-1.txt")
    main("L2/level2-2.txt")
    main("L2/level2-3.txt")
    main("L2/level2-4.txt")
    main("L2/level2-eg.txt")