# -*- coding: utf-8 -*-

from typing import List

import pytest

from snippets.data_structure.doubly_linked_list import DoublyLinkedList


def array() -> List[int]:
    return [3, 1, 4, 5, 9, 2, 6]


@pytest.fixture
def doubly_linked_list() -> DoublyLinkedList:
    return DoublyLinkedList(array=array())


class TestDoublyLinkedList:

    def test_initial_status(self, doubly_linked_list: DoublyLinkedList) -> None:
        self._execute_assert(doubly_linked_list, expected=[3, 1, 4, 5, 9, 2, 6])

    def test_insert(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.insert(5, 7)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 4, 5, 7, 9, 2, 6])

    def test_insert_twice(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.insert(5, 7)
        doubly_linked_list.insert(7, 8)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 4, 5, 7, 8, 9, 2, 6])

    def test_insert_at_end(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.insert(6, 8)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 4, 5, 9, 2, 6, 8])

    def test_remove(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.remove(4)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 5, 9, 2, 6])

    def test_remove_twice(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.remove(4)
        doubly_linked_list.remove(9)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 5, 2, 6])

    def test_remove_at_top(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.remove(3)

        self._execute_assert(doubly_linked_list, expected=[1, 4, 5, 9, 2, 6])

    def test_remove_at_end(self, doubly_linked_list: DoublyLinkedList) -> None:
        doubly_linked_list.remove(6)

        self._execute_assert(doubly_linked_list, expected=[3, 1, 4, 5, 9, 2])

    def _execute_assert(
        self, doubly_linked_list: DoublyLinkedList, expected: List
    ) -> None:
        actual = doubly_linked_list.fetch_all_values()
        assert actual == expected

    @pytest.mark.parametrize(
        ("left", "mid"),
        [
            (5, 6),
            (3, 1),
            (3, 3),
        ],
    )
    def test_insert_failed_if_invalid_input_is_given(
        self, doubly_linked_list: DoublyLinkedList, left: int, mid: int
    ) -> None:
        with pytest.raises(AssertionError):
            doubly_linked_list.insert(left, mid)

    def test_insert_failed_if_same_input_are_given(
        self, doubly_linked_list: DoublyLinkedList
    ) -> None:
        doubly_linked_list.insert(5, 10)

        with pytest.raises(AssertionError):
            doubly_linked_list.insert(5, 10)

    def test_remove_failed_if_invalid_input_is_given(
        self, doubly_linked_list: DoublyLinkedList
    ) -> None:
        with pytest.raises(AssertionError):
            doubly_linked_list.remove(10)

    def test_remove_failed_if_same_input_is_given(
        self, doubly_linked_list: DoublyLinkedList
    ) -> None:
        doubly_linked_list.remove(3)

        with pytest.raises(AssertionError):
            doubly_linked_list.remove(3)
