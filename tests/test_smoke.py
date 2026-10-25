from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("    ") == "Please type a question."


def test_help_command():
    assert "lookup office" in reply("help")


def test_new_offices_lookup(): #mien co tien to test_
    assert "B.02" in reply("Phòng Đào tạo ở đâu?")
    assert "E.02" in reply("Trạm Y tế ở đâu?")


def test_unknown_suggests_supported_topic_and_example():
    response = reply("Can you help me with classrooms?")
    assert "don't know" in response
    assert "office locations" in response
    assert "Where is the Training Office?" in response


def test_fallback_does_not_change_office_lookup():
    assert reply("Where is the Training Office?") == (
        "The Training Office is in room I.101."
    )

def test_fallback_suggests_supported_topic():
    response = reply("Can you help me with classrooms?")
    assert "office locations" in response
    assert "Where is the Training Office?" in response


def test_fallback_handles_unknown_question():
    response = reply("xyzabc123")
    assert "I don't know the answer" in response
    assert "office locations" in response

def test_fallback_suggests_supported_topic():
    response = reply("Can you help me with classrooms?")
    assert "office locations" in response
    assert "Where is the Training Office?" in response


def test_fallback_handles_unknown_question():
    response = reply("xyzabc123")
    assert "I don't know the answer" in response
    assert "office locations" in response