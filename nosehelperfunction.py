from nose.tools import assert_items_equal

#helper function, used for testing and called to be used in real world
def _find_common_ngrams_helper(text, cutoff, n):
    if n<1:
        return []
    words = text.lower().split(' ')
    ngram_counts = {}
    for start in range(len(words) +1 - n):
        ngram = ' '.join(words[start:start+n])
        current_count = ngram_counts.get(ngram, 0)
        ngram_counts[ngram] = current_count + 1
    
    result = []
    for ngram, count in ngram_counts.items():
        if count >= cutoff:
            result.append(ngram)
        
    return result

def find_common_ngrams(filename, cutoff, n):
    return _find_common_ngrams_helper(open(filename).read(), cutoff, n)

# in real world
find_common_ngrams('great_expectations_complete.txt', 15, 4)

# in testing
text = "it was the best of times it was the worst of times"
assert_items_equal(
    _find_common_ngrams_helper(text, 2, 1),
    ['it', 'was', 'the', 'of', 'times'])
