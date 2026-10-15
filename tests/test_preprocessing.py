from news_classifier.preprocessing import preprocess_sent, cleaning_strings

def test_markup_and_contact_text_are_removed():
    assert preprocess_sent('<p>뉴스 123</p> https://example.com a@example.com') == '뉴스 NUM'

def test_numeric_mask_does_not_corrupt_words():
    assert preprocess_sent('NUM MUSIC 42') == 'NUM MUSIC NUM'

def test_punctuation_tokenization():
    assert cleaning_strings('뉴스, 42!') == '뉴스 , NUM !'
