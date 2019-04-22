from journeypy.core.data.value.Values import *


def test_value_holder_entry_eq():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(object, ObjectHolder)
    assert vhe1 == vhe2, "Test Failed"


def test_value_holder_entry_nq():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(str, StringHolder)
    assert vhe1 != vhe2, "Test Failed"


def test_value_holder_entry_lt():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(str, StringHolder)
    assert vhe2 < vhe1, "Test Failed"


def test_value_holder_entry_le_when_equal():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(object, ObjectHolder)
    assert vhe2 <= vhe1, "Test Failed"


def test_value_holder_entry_le_when_less():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(str, StringHolder)
    assert vhe2 <= vhe1, "Test Failed"


def test_value_holder_entry_gt():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(str, StringHolder)
    assert vhe1 > vhe2, "Test Failed"


def test_value_holder_entry_ge_when_equal():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(object, ObjectHolder)
    assert vhe1 >= vhe2, "Test Failed"


def test_value_holder_entry_ge_when_less():
    vhe1 = ValueHolderEntry(object, ObjectHolder)
    vhe2 = ValueHolderEntry(str, StringHolder)
    assert vhe1 >= vhe2, "Test Failed"


def test_get_new_value_holder_for_string_holder_returned_for_string():
    vh=ValueHolder.get_new_value_holder_for("123")
    assert type(vh) == StringHolder, "Test Failed"
    assert vh.value == "123", "Test Failed"


def test_get_new_value_holder_for_integer_holder_returned_for_int():
    vh=ValueHolder.get_new_value_holder_for(123)
    assert type(vh) == IntegerHolder, "Test Failed"
    assert vh.value == 123, "Test Failed"


def test_get_new_value_holder_for_none_holder_returned_for_none():
    vh = ValueHolder.get_new_value_holder_for(None)
    assert type(vh) == NoneHolder, "Test Failed"
    assert vh.value is None, "Test Failed"


def test_get_new_value_holder_for_object_holder_returned_for_object():
    obj = object()
    vh = ValueHolder.get_new_value_holder_for(obj)
    assert type(vh) == ObjectHolder, "Test Failed"
    assert vh.value == obj, "Test Failed"
