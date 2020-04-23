"""Core utilities."""
import gzip
import re
import pandas as pd

FASTA_HEADER_REGEX = re.compile(
    r'\>(\w+)\|(\w+)\|(\w+)\s(.*)\sOS=(.*)\sOX='
    r'(\d+)\s(GN=(.*)\s)?PE=(\d+)\sSV=(\d+)'
)

FASTA_HEADER_STR = (
    '{db}|{accession_number}|{entry_name} {recommended_name} '
    'OS={organism_name} OX={organism_id} GN={gene_name} '
    'PE={protein_existence} SV={sequence_version}'
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


def csv_to_fasta(filepath, chunk_size):
    """
    Parse csv (from upfp parsed fasta) and return an iterator of sequences.

    Args:
        filepath (str): path to the file.
        chunk_size (int): number of rows to process at a time.
    Returns:
        str: generator of chunks of fasta sequences.
    """
    for chunk in pd.read_csv(filepath, chunksize=chunk_size, index_col=0):
        sequences = []
        for _, row in chunk.iterrows():
            header = make_header(row)
            sequences.append(format_fasta(header, row['sequence']))
        yield ''.join(sequences)


def smi_to_fasta(filepath, chunk_size):
    """
    Parse .smi (tsv) and return an iterator of sequences.

    Args:
        filepath (str): path to the file. The file is expected to have sequence
            and accession_number as first columns.
        chunk_size (int): number of rows to process at a time.
    Returns:
        str: generator of chunks of fasta sequences.
    """

    chunks = pd.read_csv(filepath, chunksize=chunk_size, sep='\t', header=None)
    for chunk in chunks:
        sequences = []
        for _, row in chunk.iterrows():
            header = row.iloc[1]
            sequences.append(format_fasta(header, row.iloc[0]))
        yield ''.join(sequences)


def format_fasta(header, sequence, line_length=60):
    """Format sequence as in fasta with leading '>'.

    Args:
        header (str): description.
        sequence (str): sequence to wrap over lines.
        line_length (int, optional): line break. Defaults to 80.

    Returns:
        str: fasta file entry.
    """
    lines = ['>{header}\n'.format(header=header)]
    for i in range(0, len(sequence), line_length):
        lines.append(sequence[i:i + line_length] + '\n')

    return ''.join(lines)


def make_header(header_kwargs):
    """Fill values in FASTA_HEADER_STR to recreate full header.

    Args:
        header_kwargs ([dict or pandas.Series]): keyword arguments

    Returns:
        str: FASTA entry header content (no '<')
    """
    return FASTA_HEADER_STR.format(**header_kwargs)
