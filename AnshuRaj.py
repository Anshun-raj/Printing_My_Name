class Naam:
    def nameA(self):
        for i in range(7):
            for j in range(4):
                if (i == 0 and j % 4 != 0 or j == 0) or (i == 1 and j % 3 == 0) or (i == 2 and j % 3 == 0) or (
                        i == 3 and j % 4 != 0 or j == 0) or (i == 4 and j % 3 == 0) or (i == 5 and j % 3 == 0) or (
                        i == 6 and j % 3 == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def nameN(self):
        for i in range(5):
            for j in range(5):
                if (i == 0 and j % 4 == 0) or (i == 1 and j % 4 == 1 or j % 4 == 0) or (
                        i == 2 and j % 4 == 2 or j % 4 == 0) or (i == 3 and j % 4 == 3 or j % 4 == 0) or (
                        i == 4 and j % 4 == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def nameS(self):
        for i in range(10):
            for j in range(4):
                if (i == 0 and j % 4 != 0) or (i >= 1 and i <= 3 and j == 0) or (i - j == 3) or (
                        i >= 6 and i <= 8 and j == 3) or (i == 9 and j >= 0 and j <= 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def nameH(self):
        for i in range(5):
            for j in range(5):
                if (i == 0 and j % 3 == 0) or (i == 1 and j % 3 == 0) or (i == 2 and j % 1 == 0 and j < 4) or (
                        i == 3 and j % 3 == 0) or (i == 4 and j % 3 == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def nameU(self):
        for i in range(5):
            for j in range(4):
                if (i == 0 and j % 3 == 0) or (i == 1 and j % 3 == 0) or (i == 2 and j % 3 == 0) or (
                        i == 3 and j % 3 == 0) or (i == 4 and j % 3 != 0):
                    print("* ", end=" ")
                else:
                    print(" ", end=" ")
            print()

    def nameR(self):
        for i in range(7):
            for j in range(5):
                if (i == 0 and j >= 1 and j <= 2) or (i >= 1 and i <= 2 and j % 3 == 0) or (
                        i == 3 and j % 2 == 0 and j != 4) or (i == 4 and j >= 0 and j <= 1) or (
                        i == 5 and j % 2 == 0 and j != 4) or (i == 6 and j % 3 == 0) or (i == 7 and j == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()



    def nameJ(self):
        for i in range(7):
            for j in range(7):
                if (i == 0 and j >= 0 and j <= 7) or (i == 1 and j == 3) or (i == 2 and j == 3) or (
                        i == 3 and j == 3) or (i == 4 and j % 3 == 0 and j != 6) or (
                        i == 5 and j % 3 == 0 and j != 6) or (i == 6 and j >= 0 and j <= 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

obj=Naam()
obj.nameA()
obj.nameN()
obj.nameS()
obj.nameH()
obj.nameU()
obj.nameR()
obj.nameA()
obj.nameJ()
