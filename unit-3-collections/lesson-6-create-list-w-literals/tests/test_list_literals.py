def test_list_literals():
    assert type(heterogeneous) == list
    assert any(isinstance(x, bool) for x in heterogeneous)
    assert any(isinstance(x, int) for x in heterogeneous)
    assert any(isinstance(x, str) for x in heterogeneous)