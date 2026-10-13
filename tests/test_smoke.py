from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."

def test_new_offices_lookup(): #mien co tien to test_
    assert "B.02" in reply("Phòng Đào tạo ở đâu?")
    assert "E.02" in reply("Trạm Y tế ở đâu?")