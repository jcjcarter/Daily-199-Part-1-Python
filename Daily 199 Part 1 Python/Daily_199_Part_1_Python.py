import sys

# print without newline
def printnnl(string):
    sys.stdout.write(string)


def print_digit(string):
    indexes = []
    for char in string:
        indexes.append(int(char))

    digits = [
        [" _ ", "| |", "|_|"]  # 0
        , ["   ", "  |", "  |"]  # 1
        , [" _ ", " _|", "|_ "]  # 2
        , [" _ ", " _|", " _|"]  # 3
        , ["   ", "|_|", "  |"]  # 4
        , [" _ ", "|_ ", " _|"]  # 5
        , [" _ ", "|_ ", "|_|"]  # 6
        , [" _ ", "  |", "  |"]  # 7
        , [" _ ", "|_|", "|_|"]  # 8
        , [" _ ", "|_|", " _|"]  # 9
    ]

    level = 0
    depth = 3
    while level < depth:
        for index in indexes:
            printnnl(digits[index][level])
        printnnl("\n")
        level += 1


print_digit("000000000")
print_digit("111111111")
print_digit("490067715")