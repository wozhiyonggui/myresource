# -*- coding: UTF-8 -*-
"""
https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_subsequence#Python
"""
__author__ = 'howtoesc@gmail.com'


def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C


def printDiff(C, X, Y, i, j):
    if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
        printDiff(C, X, Y, i - 1, j - 1)
        print "  " + X[i - 1]
    else:
        if j > 0 and (i == 0 or C[i][j - 1] >= C[i - 1][j]):
            printDiff(C, X, Y, i, j - 1)
            print "+ " + Y[j - 1]
        elif i > 0 and (j == 0 or C[i][j - 1] < C[i - 1][j]):
            printDiff(C, X, Y, i - 1, j)
            print "- " + X[i - 1]


def printDiffs(C, X, Y, i, j):
    if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:

        return printDiffs(C, X, Y, i - 1, j - 1) + ["="]
    else:
        if j > 0 and (i == 0 or C[i][j - 1] >= C[i - 1][j]):
            return printDiffs(C, X, Y, i, j - 1) + ["+"]

        elif i > 0 and (j == 0 or C[i][j - 1] < C[i - 1][j]):
            return printDiffs(C, X, Y, i - 1, j) + ["-"]
    return []


def diff(X, Y):
    return printDiffs(LCS(X, Y), X, Y, len(X), len(Y))


if __name__ == '__main__':
    X = [
        "This part of the document has stayed",
        "the same from version to version.",
        "",
        "This paragraph contains text that is",
        "outdated - it will be deprecated '''and'''",
        "deleted '''in''' the near future.",
        "",
        "It is important to spell check this",
        "dokument. On the other hand, a misspelled",
        "word isn't the end of the world.",
    ]
    Y = [
        "This is an important notice! It should",
        "therefore be located at the beginning of",
        "this document!",
        "",
        "This part of the document has stayed",
        "the same from version to version.",
        "",
        "It is important to spell check this",
        "document. On the other hand, a misspelled",
        "word isn't the end of the world. This",
        "paragraph contains important new",
        "additions to this document.",
    ]

    C = LCS(X, Y)
    printDiff(C, X, Y, len(X), len(Y))
    print diff(X, Y)
