#!/usr/bin/python3.5

class main:
    def __init__(self, file):
        self.file = file
        self.reader()
        timestamps = sorted(self.trans.keys())
        for i in timestamps:
            self.submit_transaction(i)
        self.ouput()


    def submit_transaction(self, tid):
        src = self.trans[tid][0]
        dest = self.trans[tid][1]
        amt = int(self.trans[tid][2])
        self.acc[dest] += amt
        self.acc[src] -= amt

    def ouput(self):
        print(self.acc)
        file = open(self.file+"_out", "w")
        file.write("%i\n"%self.acc_num)
        for (i, j) in self.acc.items():
            file.write("%s %s\n"%(i, j))
        pass

    def reader(self):
        print("reading"+self.file)
        read = open(self.file)
        self.acc_num = int(read.readline())
        self.acc = {}
        for i in range(0, self.acc_num):
            j = read.readline()
            j = j.split(" ")
            self.acc[j[0]]=int(j[1])

        self.trans_num = int(read.readline())
        self.trans = {}
        for i in range(0, self.trans_num):
            j = read.readline().replace("\n", "")
            j = j.split(" ")
            self.trans[j[3]]=(j[0], j[1], j[2])


if __name__ == "__main__":
    main("L2/level1-1.txt")
    main("L2/level1-2.txt")
    main("L2/level1-3.txt")
    main("L2/level1-4.txt")
    main("L2/level1-eg.txt")
