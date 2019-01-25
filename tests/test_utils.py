from unittest import TestCase

from postfinance.utils import dict_to_ordered_qs


class UtilsTestCase(TestCase):
    def test_dict_to_ordered_qs_basic(self):
        qs = dict_to_ordered_qs({"Z": "x", "A": "b"}, "-")
        self.assertEqual("A=b-Z=x", qs)

    def test_dict_to_ordered_qs_various_types(self):
        # non-str values, and non-str keys
        qs = dict_to_ordered_qs({"A": 1, 2: 5}, "-")
        self.assertEqual("2=5-A=1", qs)

    def test_dict_item_fields_order(self):
        qs = dict_to_ordered_qs({"ITEMNAME1": "Foo", "ITEMNAME11": "Bar", "ITEMNAME2": "Zoo"}, "-")
        self.assertLess(qs.find("ITEMNAME1"), qs.find("ITEMNAME2"))
        self.assertLess(qs.find("ITEMNAME2"), qs.find("ITEMNAME11"))

