"""Tests for the upfp.iterator submodule."""
import unittest
from upfp.iterator import chunker


class TestIterator(unittest.TestCase):
    """Testing upfp.iterator submodule."""

    def test_chunker(self):
        """Test chunker."""
        a_list = list(range(10))
        chunks = list(chunker(a_list, 4))
        self.assertEqual(
            3,
            len(chunks)
        )
        self.assertEqual(
            [0, 1, 2, 3],
            list(chunks[0])
        )
        self.assertEqual(
            [4, 5, 6, 7],
            list(chunks[1])
        )
        self.assertEqual(
            [8, 9],
            list(chunks[2])
        )