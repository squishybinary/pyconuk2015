#conventions for nose (conventions over configuration)
#Files that contain test code -> name start with test
#tests should be in Functions -> name  start with test

from nose.tools import assert_equal

def find_common_ngrams(text, cutoff, n):
    if n < 1:
        return []
    words = text.lower().split(' ')
    result = []
    for start in range(len(words) +1 - n):
        ngram = ' '.join(words[start:start+n])
        if text.count(ngram) >= cutoff and ngram not in result:
            result.append(ngram)
            
    return result

text = "it was the best of times it was the worst of times"

#replace with assert_items_equal with the first two tests
def test_single_words():
    assert_equal(find_common_ngrams(text, 2, 1),['it', 'was', 'the', 'of', 'times'])

def test_all_words():
    assert_equal(find_common_ngrams(text, 1, 1),['it', 'was', 'the', 'best', 'of', 'times', 'worst'])

def test_small_n():
    assert_equal(find_common_ngrams(text, 2, 3),['it was the'])

def test_large_n():
    assert_equal(find_common_ngrams(text, 1, 12),['it was the best of times it was the worst of times'])

def test_zero_n():
    assert_equal(find_common_ngrams(text, 2, 0),[])

def test_negative_n():
    assert_equal(find_common_ngrams(text, 2, -4),[])
