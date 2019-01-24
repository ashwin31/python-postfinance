from postfinance.utils import dict_to_ordered_qs


def test_dict_to_ordered_qs_test():
    qs = dict_to_ordered_qs({"Z": "x", "A": "b"}, "-")
    assert qs == "A=b-Z=x"

    # non-str values, and non-str keys
    qs = dict_to_ordered_qs({'A': 1, 2: 5}, "-")
    assert qs == "2=5-A=1"
