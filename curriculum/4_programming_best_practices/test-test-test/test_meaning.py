# function to test
def get_answer():
    return 42


# actual test
def test_answer_to_file_is_42():
    assert get_answer() == 42
