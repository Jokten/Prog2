class Holder:
    def __init__(self):
        self.val = 5

    def __iter__(self):
        yield 4


    def return_val(self):
        while True:
            yield self.val


def main():
    print('hej')




if __name__ == '__main__':
    main()
