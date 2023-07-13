import pytest

from snippets.data_structure.range_add_sum_query import RAQ_AND_RSQ_ZERO_INDEXED


@pytest.fixture
def raq_rsq() -> RAQ_AND_RSQ_ZERO_INDEXED:
    return RAQ_AND_RSQ_ZERO_INDEXED(5)


class TestRAQ_AND_RSQ_ZERO_INDEXED:
    def test_initial_status(self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED) -> None:
        actual = raq_rsq.debug_list()
        expected = [0] * (raq_rsq.size)

        assert actual == expected

    def test_add(self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED) -> None:
        # [left, right)
        raq_rsq.add(left=0, right=5, value=3)
        actual = raq_rsq.debug_list()
        expected = [3, 3, 3, 3, 3]

        assert actual == expected

    def test_add_multiple_times(self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED) -> None:
        # [left, right)
        raq_rsq.add(left=0, right=5, value=3)
        actual = raq_rsq.debug_list()
        expected = [3] * 5
        assert actual == expected

        raq_rsq.add(left=3, right=5, value=2)
        actual = raq_rsq.debug_list()
        expected = [3, 3, 3, 5, 5]
        assert actual == expected

        raq_rsq.add(left=1, right=4, value=7)
        actual = raq_rsq.debug_list()
        expected = [3, 10, 10, 12, 5]
        assert actual == expected

        raq_rsq.add(left=0, right=1, value=1)
        actual = raq_rsq.debug_list()
        expected = [4, 10, 10, 12, 5]
        assert actual == expected

    def test_add_when_negative_value_is_given(
        self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED
    ) -> None:
        # [left, right)
        actual = raq_rsq.debug_list()
        expected = [0] * 5
        assert actual == expected

        raq_rsq.add(left=0, right=5, value=-5)
        actual = raq_rsq.debug_list()
        expected = [-5] * 5
        assert actual == expected

    def test_add_when_zero_is_given(self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED) -> None:
        # [left, right)
        actual = raq_rsq.debug_list()
        expected = [0] * 5
        assert actual == expected

        raq_rsq.add(left=0, right=5, value=0)
        assert actual == expected

    @pytest.mark.parametrize(
        ("left", "right", "expected"),
        [
            (0, 1, 4),
            (0, 2, 14),
            (0, 3, 24),
            (0, 4, 36),
            (0, 5, 41),
            (1, 2, 10),
            (1, 3, 20),
            (1, 4, 32),
            (1, 5, 37),
            (2, 3, 10),
            (2, 4, 22),
            (2, 5, 27),
            (3, 4, 12),
            (3, 5, 17),
            (4, 5, 5),
        ],
    )
    def test_range_sum(
        self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED, left: int, right: int, expected: int
    ) -> None:
        raq_rsq.add(left=0, right=5, value=3)
        raq_rsq.add(left=3, right=5, value=2)
        raq_rsq.add(left=1, right=4, value=7)
        raq_rsq.add(left=0, right=1, value=1)

        assert raq_rsq.query(left, right) == expected

    @pytest.mark.parametrize(
        ("left", "right"),
        [
            (-2, 1),
            (-1, 5),
            (0, 6),
            (0, 7),
            (-2, 6),
            (-2, 7),
            (-1, 6),
            (-1, 7),
        ],
    )
    def test_add_failed_if_invalid_input_is_given(
        self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED, left: int, right: int
    ) -> None:
        with pytest.raises(AssertionError):
            raq_rsq.add(left=left, right=right, value=1)

    @pytest.mark.parametrize(
        ("left", "right"),
        [
            (-2, 1),
            (-1, 5),
            (0, 6),
            (0, 7),
            (-2, 6),
            (-2, 7),
            (-1, 6),
            (-1, 7),
        ],
    )
    def test_range_sum_failed_if_invalid_input_is_given(
        self, raq_rsq: RAQ_AND_RSQ_ZERO_INDEXED, left: int, right: int
    ) -> None:
        with pytest.raises(AssertionError):
            raq_rsq.query(left, right)
