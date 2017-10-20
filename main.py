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
        if re.search('CAT\d\d\w{10}', aid):
            valid = True
            chars = {}
            acc_id = aid[5:] + "CAT00"
            check = 0

            for c in acc_id:
                check += ord(c)
            check = 98-check%97

            if not check == int(aid[3:5]):
                print(aid)
                valid = False

            for char in aid[5:]:
                if chars.get(char):
                    chars[char] += 1
                else:
                    chars[char] = 1

            for char in chars.keys():
                if char.isupper():
                    print(aid)
                    if chars[char] != chars.get(char.lower()):
                        valid = False
                else:
                    print(aid)
                    if chars[char] != chars.get(char.upper()):
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