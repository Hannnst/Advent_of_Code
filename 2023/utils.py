# A file for recurring functionality for global usage

def readFile(filename):
    """ Reads a file and returns a list of its contents """

    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines
