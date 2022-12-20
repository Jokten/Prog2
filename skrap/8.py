import numpy as np

def file_reader(filename):
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f'File {filename} not found')
        return

def main():
    filename = 'input.txt'
    data = file_reader(filename)
    # Split each line into a list of integers and make it a numpy array
    data = [np.array([int(x) for x in list(line)]) for line in data]
    print(data)


if __name__ == '__main__':
    main()