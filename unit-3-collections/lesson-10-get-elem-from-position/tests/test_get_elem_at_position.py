def test_get_elem_at_position():
    assert get_second_elem(["not this one", "this one!!!"]) == "this one!!!"