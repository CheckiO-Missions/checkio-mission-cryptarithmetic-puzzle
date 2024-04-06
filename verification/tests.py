"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

numeral_words_dic = {
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    9: 'NINE',
    10: 'TEN',
    11: 'ELEVEN',
    12: 'TWELVE',
    16: 'SIXTEEN',
    20: 'TWENTY',
    40: 'FORTY',
    50: 'FIFTY',
    60: 'SIXTY',
    70: 'SEVENTY',
    80: 'EIGHTY',
    90: 'NINETY',
}


def make_numeral_words_tests(*tests):
    for test in tests:
        nums, answer = test
        yield {
            'input': [[numeral_words_dic[n] for n in nums]],
            'answer': {a: i for i, a in enumerate(answer) if a != ' '},
        }


TESTS = {
    "Basics": [
        {
            'input': [['SEND', 'MORE', 'MONEY']],
            'answer': {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2},
        },
        {
            'input': [['BLACK', 'GREEN', 'ORANGE']],
            'answer': {'A': 2, 'C': 0, 'R': 3, 'K': 8, 'G': 5, 'N': 6, 'O': 1, 'B': 7, 'L': 9, 'E': 4},
        },
        {
            'input': [['POTATO', 'TOMATO', 'PUMPKIN']],
            'answer': {'N': 2, 'O': 6, 'I': 7, 'T': 8, 'A': 4, 'K': 9, 'M': 3, 'P': 1, 'U': 0},
        },
        {
            'input': [['KYOTO', 'OSAKA', 'TOKYO']],
            'answer': {'A': 0, 'K': 4, 'O': 3, 'S': 2, 'Y': 1, 'T': 7},
        },
    ],
    "Numeral": list(make_numeral_words_tests(
        ([6, 7, 7, 20], 'XTNWYISVE '),
        ([10, 10, 40, 60], 'NIFSXEYRTO'),
        ([1, 9, 20, 50, 80], 'GHYTEIWFNO'),
        ([1, 2, 3, 3, 11, 20], 'VETWYNOLRH'),
        ([6, 7, 9, 12, 16, 20, 70], 'XTLINWESYV'),
        ([1, 2, 5, 9, 11, 12, 50, 90], 'VTFOLEINWY'),
    )),
}
