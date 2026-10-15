# test_issue10.py
from assistant_rules import reply

def test_partial_office_name():
    assert "1.101" in reply("where is training")

def test_another_partial_office_name():
    assert "2.202" in reply("lookup IT office")

def test_no_false_match_inside_word():
    assert "couldn't find" in reply("where can I submit my form")

def test_prefix_match():
    assert "1.101" in reply("where is train")
