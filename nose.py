
text = 'it was the best of times it was the worst of times'

def find_common_ngrams(text, cutoff, n):

    #special case for n less than one, I instead directly looked for ''
    if n < 1:
        return []

    
    words = text.lower().split(' ')
    result = []
    for start in range(len(words) +1 - n):
        ngram = ' '.join(words[start:start+n])
        
        # only add a ngram to the result if it's not already in there
        if text.count(ngram) >= cutoff and ngram not in result and ngram != '':
            result.append(ngram)
            
    return result

assert find_common_ngrams(text, 2, 2) == ['it was', 'was the', 'of times']
assert find_common_ngrams(text, 2, 1) == ['it', 'was', 'the', 'of', 'times']
#doesn't wrap around the input. So 1 assert of length 3 words
assert find_common_ngrams(text, 2, 3) == ['it was the']
assert find_common_ngrams(text, 1, 12) == ['it was the best of times it was the worst of times']

assert find_common_ngrams(text, 1, 0) == []

#Test Suite
# test different cutoffs for the same n
assert find_common_ngrams(text, 2, 1) == ['it', 'was', 'the', 'of', 'times']
assert find_common_ngrams(text, 1, 1) == ['it', 'was', 'the', 'best', 'of', 'times', 'worst']

# test different n with the same cutoff
assert find_common_ngrams(text, 2, 3) == ['it was the']
assert find_common_ngrams(text, 1, 12) == ['it was the best of times it was the worst of times']

# test crazy values of n
assert find_common_ngrams(text, 2, 0) == []
assert find_common_ngrams(text, 2, -4) == []
