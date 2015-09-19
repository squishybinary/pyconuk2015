from nose.tools import assert_equal, assert_items_equal

def find_common_ngrams(text, cutoff, n):
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


text = "it was the best of times it was the worst of times"

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
