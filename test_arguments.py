from arguments import add_to_list

list1 = add_to_list(1)
assert list1 == [1], "New list does not consist of just [1]"

list1 = add_to_list(2, list1)
assert list1 ==[1, 2], "New list does not consist of [1, 2]"

list3 = add_to_list(3)
assert list1 == [1, 2], "list1 does not consist of [1, 2]"

list4 = add_to_list("A")
assert list4 == ["A"], "list4 does not consist of ['A']"

add_to_list("B", list4)
assert list4 == ["A", "B"], "list4 does not consist of ['A', 'B']"