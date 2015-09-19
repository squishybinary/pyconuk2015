from nose.tools import assert_equal, with_setup

def remove_long_words(word_list, max):
    for word in list(word_list):
        if len(word) > max:
            word_list.remove(word)         

words = []
def setup_words():
    global words
    words = "it was the best of times it was the worst of times".split()

@with_setup(setup_words)
def test_two():    
    remove_long_words(words, 2)
    assert_equal(words, ['it', 'of', 'it', 'of'])

@with_setup(setup_words)
def test_four():
    remove_long_words(words, 4)
    assert_equal(words, ['it', 'was', 'the', 'best', 'of', 'it', 'was', 'the', 'of'])
