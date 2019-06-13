"""Iterator utilities."""
import itertools


def chunker(iterable, chunk_size):
    """
    A chunker for iterators.

    Args:
        iterable (iterable-like): the iterable to be chunked.
        chunk_size (int): size of the chunk.
    Returns:
        A chunked iterator.
    """
    iterator = iter(iterable)
    while True:
       chunk = tuple(
           itertools.islice(
               iterator,
               chunk_size   
            )
        )
       if not chunk:
           return
       yield chunk