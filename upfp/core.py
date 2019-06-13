"""Core utilities."""
import gzip
import re

FASTA_HEADER_REGEX = re.compile(
    r'\>(\w+)\|(\w+)\|(\w+)\s(.*)\sOS=(.*)\sOX='
    r'(\d+)\s(GN=(.*)\s)?PE=(\d+)\sSV=(\d+)'
)


def parse_fasta(filepath, gzipped=True):
    """
    Parse a fasta and return an iterator of sequences.

    Args:
        filepath (str): path to the file.
        gzipped (bool): is the file compressed.
    Returns:
        an iterator of parsed sequences, i.e., a dictionary
        containing the header and the sequence.
    """
    # conditional setup of the I/O functions
    open_fn = open
    parse_line_fn = lambda line: line.strip()
    if gzipped:
        open_fn = gzip.open
        parse_line_fn = lambda line: line.strip().decode()
    # initialize an object to store the sequence and the header
    sequence = {}
    with open_fn(filepath) as fp:
        for line in fp:
            line = parse_line_fn(line)
            match = FASTA_HEADER_REGEX.match(line)
            if match:
                # yield the previously parsed sequence if properly parsed
                if len(sequence) > 1:
                    yield sequence
                # parse the new header
                groups = match.groups()
                # assemble the sequence dictionary and prepare for parsing
                # the sequence
                sequence = {
                    'db': groups[0],
                    'accession_number': groups[1],
                    'entry_name': groups[2],
                    'recommended_name': groups[3],
                    'organism_name': groups[4],
                    'organism_id': groups[5],
                    'gene_name': groups[7],
                    'protein_existence': groups[8],
                    'sequence_version': groups[9],
                    'sequence': ''
                }
            else:
                # accumulate the sequence
                sequence['sequence'] += line
        # yield the last sequence
        yield sequence