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


def make_answer_dict(alphabets):
    return {a: i for i, a in enumerate(alphabets) if a != ' '}


def make_tests(*tests):
    for test in tests:
        words, answer = test
        yield {
            'input': [words.split()],
            'answer': make_answer_dict(answer),
        }


def make_numeral_words_tests(*tests):
    for test in tests:
        nums, answer = test
        yield {
            'input': [[numeral_words_dic[n] for n in nums]],
            'answer': make_answer_dict(answer)
        }


TESTS = {
    "Basics": list(make_tests(
        #                                0123456789
        ('SEND MORE MONEY',             'OMY  ENDRS'),
        ('BLACK GREEN ORANGE',          'COAREGNBKL'),
        ('POTATO TOMATO PUMPKIN',       'UPNMA OITK'),
        ('KYOTO OSAKA TOKYO',           'AYSOK  T  '),
    )),
    "Numeral": list(make_numeral_words_tests(
        #                                0123456789
        ([6, 7, 7, 20],                 'XTNWYISVE '),
        ([10, 10, 40, 60],              'NIFSXEYRTO'),
        ([1, 9, 20, 50, 80],            'GHYTEIWFNO'),
        ([1, 2, 3, 3, 11, 20],          'VETWYNOLRH'),
        ([6, 7, 9, 12, 16, 20, 70],     'XTLINWESYV'),
        ([1, 2, 5, 9, 11, 12, 50, 90],  'VTFOLEINWY'),
    )),
}
