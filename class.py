class car:
    # number = 3434
    # name = "demo"
    def __init__(self,a,b):
        self.number = a
        self.name = b


def main():
    c = car(7806,"bmw")
    # c.number = 7806
    # c.name = "bmw"

    d = car(455,"dsdsfs")
    d.name = "toyota"
    d.number = 458

    print(c.name + " " + str(c.number))
    print(d.name + " " + str(d.number))

if __name__ == "__main__":
    main()