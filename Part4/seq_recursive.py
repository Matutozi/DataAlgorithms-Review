"""seq1 - serendipitious
seq2 - precipitation
"""

def len_lcs(seq1, seq2):
    pass

#Solution

def lcs_recursion(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) and idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursion(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursion(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursion(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)
    