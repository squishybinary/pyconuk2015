#This fails on asserts. Switch over to nose to understand
#As doesn't provide enough information

from nose.tools import assert_equal, assert_items_equal

text = 'it was the best of times it was the worst of times'

def count_ngrams(text, cutoff, n):
    words = text.lower().split(' ')
    ngram_counts = {}
    for start in range(len(words) +1 - n):
        ngram = ' '.join(words[start:start+n])
        current_count = ngram_counts.get(ngram, 0)
        ngram_counts[ngram] = current_count + 1

    return ngram_counts

def find_common_ngrams(text, cutoff, n):
    if n < 1:
        return []
    # first generate a dict of n-gram counts
    words = text.lower().split(' ')
    ngram_counts = {}
    for start in range(len(words) +1 - n):
        ngram = ' '.join(words[start:start+n])
        current_count = ngram_counts.get(ngram, 0)
        ngram_counts[ngram] = current_count + 1
    
    # now return just the ngrams with count > cutoff
    result = []
    for ngram, count in ngram_counts.items():
        if count >= cutoff:
            result.append(ngram)
        
    return result

'''
assert find_common_ngrams(text, 2, 2) == ['it was', 'was the', 'of times']
assert find_common_ngrams(text, 1, 0) == []

#Test Suite
# test different cutoffs for the same n
assert find_common_ngrams(text, 2, 1) == ['it', 'was', 'the', 'of', 'times']
assert find_common_ngrams(text, 1, 1) == ['it', 'was', 'the', 'best', 'of', 'times', 'worst']

# test different n with the same cutoff
assert find_common_ngrams(text, 2, 3) == ['it was the']
#doesn't wrap around the input. So 1 assert of length 3 words
assert find_common_ngrams(text, 1, 12) == ['it was the best of times it was the worst of times']

# test crazy values of n
assert find_common_ngrams(text, 2, 0) == []
assert find_common_ngrams(text, 2, -4) == []
'''

#new nose testing
def test_single_words():
    assert_items_equal(find_common_ngrams(text, 2, 1),['it', 'was', 'the', 'of', 'times'])

def test_all_words():
    assert_items_equal(find_common_ngrams(text, 1, 1),['it', 'was', 'the', 'best', 'of', 'times', 'worst'])

def test_small_n():
    assert_equal(find_common_ngrams(text, 2, 3),['it was the'])

def test_large_n():
    assert_equal(find_common_ngrams(text, 1, 12),['it was the best of times it was the worst of times'])

def test_zero_n():
    assert_equal(find_common_ngrams(text, 2, 0),[])

def test_negative_n():
    assert_equal(find_common_ngrams(text, 2, -4),[])
