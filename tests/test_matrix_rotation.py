# -*- coding: utf-8 -*-


from snippets.math.matrix_rotation import rotate_90_degrees_to_right


class TestMatrixRotation:
    def test_rotate_90_degrees_to_right(self):
        array = [[0, 1, 1], [1, 0, 0], [0, 1, 0]]

        # 1st.
        actual = rotate_90_degrees_to_right(array)
        expected = [[0, 1, 0], [1, 0, 1], [0, 0, 1]]
        assert actual == expected

        # 2nd.
        actual = rotate_90_degrees_to_right(actual)
        expected = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
        assert actual == expected

        # 3rd.
        actual = rotate_90_degrees_to_right(actual)
        expected = [[1, 0, 0], [1, 0, 1], [0, 1, 0]]
        assert actual == expected

        # 4th (= array).
        actual = rotate_90_degrees_to_right(actual)
        expected = array
        assert actual == expected
