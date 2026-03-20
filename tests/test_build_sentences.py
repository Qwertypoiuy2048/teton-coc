import pytest
import json
from build_sentences import (
    get_seven_letter_word, 
    parse_json_from_file, 
    choose_sentence_structure,
    get_pronoun, 
    get_article, 
    get_word, 
    fix_agreement, 
    build_sentence, 
    structures)

def test_get_seven_letter_word(mocker):
    # Arrange - Mock the input function
    mocker.patch("builtins.input", return_value="abcdefg")
    # Act - Call the function under test
    result = get_seven_letter_word()
    # Assert -  the result
    assert result == "ABCDEFG"


def test_get_seven_letter_word_fail(mocker):

    # Arrange
    mocker.patch("builtins.input", return_value="foo")

    with pytest.raises(ValueError):  # Assert
        get_seven_letter_word()  # Act

    

def test_parse_json_from_file(tmp_path):
    # Create a temporary file with test data
    test_data = {"adjectives": ["",""], "nouns": ["",""]}
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(test_data, f)

    # Call the function under test
    result = parse_json_from_file(file_path)

    # Assert the result
    assert result == test_data

def test_choose_sentence_structure():
    assert choose_sentence_structure() in structures

def test_get_pronoun(mocker):
    mocker.patch("random.choice", return_value="he")
    assert get_pronoun() == "he"
    

def test_get_article(mocker):
    mocker.patch("random.choice", return_value="a")
    assert get_article() == "a"
    

def test_get_word():
    letters = ["A", "B", "C", "D", "E", "F"]
    assert get_word('B', letters) == "B"
    

def test_fix_agreement_a():
    sentence = ['we', 'quickly', 'run', 'a', 'happy', 'apple', 'about', 'the', 'happy', 'apples']
    fix_agreement(sentence)
    assert sentence == ['we', 'quickly', 'run', 'an', 'happy', 'apple', 'about', 'the', 'happy', 'apples']


def test_fix_agreement_the():
    sentence = ['the', 'smart', 'mountain', 'quickly', 'listen', 'among', 'a', 'happy', 'sun']
    fix_agreement(sentence)
    assert sentence == ['the', 'smart', 'mountain', 'quickly', 'listens', 'among', 'a', 'happy', 'sun']

def test_fix_agreement_he_she():
    sentence = ['she', 'seldom', 'frown', 'the', 'tall', 'phone', 'after', 'the', 'dumb', 'cloud']
    fix_agreement(sentence)
    assert sentence == ['she', 'seldom', 'frowns', 'the', 'tall', 'phone', 'after', 'the', 'dumb', 'cloud']


def test_build_sentence(mocker):
    mocker.patch("build_sentences.get_word", return_value="apples")
    mocker.patch("build_sentences.get_article", return_value="apples")
    mocker.patch("build_sentences.get_pronoun", return_value="apples")
    assert build_sentence('abcdefg', ['ART', 'ADJ', 'NOUN', 'VERB', 'ADV', 'PREP', 'PRO'], {'adjectives':{},'nouns':{},'verbs':{},'adverbs':{},'prepositions':{},'pronouns':{}}) == \
        "Apples apples apples apples apples apples apples"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])


"""
How to - Coverage Reports:

#!  py -m coverage run -m pytest test_build_sentences.py
Returns: 
#*    collected 11 items                                                                                                                                                                 
#*
#*    test_build_sentences.py ...........                                                                                                     [100%] 
#*
#*    ============================================================= 11 passed in 0.24s ============================================================= 


#* Similar report to this :
#* if __name__ == "__main__":
#!    pytest.main(["-v", "--tb=line", "-rN", __file__])
Returns:
#*    collected 11 items                                                                                                                                      
#*
#*    test_build_sentences.py::test_get_seven_letter_word PASSED                                                                    [  9%] 
#*    test_build_sentences.py::test_get_seven_letter_word_fail PASSED                                                               [ 18%] 
#*    test_build_sentences.py::test_parse_json_from_file PASSED                                                                     [ 27%]
#*    test_build_sentences.py::test_choose_sentence_structure PASSED                                                                [ 36%] 
#*    test_build_sentences.py::test_get_pronoun PASSED                                                                              [ 45%] 
#*    test_build_sentences.py::test_get_article PASSED                                                                              [ 54%] 
#*    test_build_sentences.py::test_get_word PASSED                                                                                 [ 63%] 
#*    test_build_sentences.py::test_fix_agreement_a PASSED                                                                          [ 72%] 
#*    test_build_sentences.py::test_fix_agreement_the PASSED                                                                        [ 81%] 
#*    test_build_sentences.py::test_fix_agreement_he_she PASSED                                                                     [ 90%] 
#*    test_build_sentences.py::test_build_sentence PASSED                                                                           [100%] 
#*
#*    ======================================================== 11 passed in 0.07s ======================================================== 



#!  py -m coverage report -m
Returns:
#*    Name                      Stmts   Miss  Cover   Missing
#*    -------------------------------------------------------
#*    build_sentences.py           67      6    91%   106-110, 113
#*    test_build_sentences.py      48      1    98%   89
#*    -------------------------------------------------------
#*    TOTAL                       115      7    94%
"""