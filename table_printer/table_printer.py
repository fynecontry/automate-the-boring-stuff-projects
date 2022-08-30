#!/usr/bin/env python3

def printTable(tableData):
    '''Prints tablular data of list passed to screen'''

    # get the maximum width for each column
    #colWidths = []
    #for index, row in tableData:
    #    colWidths[index] = len(max(row, key=len))

    colWidths = [len(max(row, key=len)) for row in tableData]

    # Print table using each colwidth for max right-justified
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]) + ' ', end='')
        print()


def main():
    '''Main program'''

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)

if __name__ == "__main__":
    main()
