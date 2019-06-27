[![Build Status](https://travis-ci.org/drugilsberg/uniprot_fasta_parser.svg?branch=master)](https://travis-ci.org/drugilsberg/uniprot_fasta_parser)
[![codecov](https://codecov.io/gh/drugilsberg/uniprot_fasta_parser/branch/master/graph/badge.svg)](https://codecov.io/gh/drugilsberg/uniprot_fasta_parser)
[![Updates](https://pyup.io/repos/github/drugilsberg/uniprot_fasta_parser/shield.svg)](https://pyup.io/repos/github/drugilsberg/uniprot_fasta_parser/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/upfp.svg)](https://badge.fury.io/py/upfp)
# uniprot_fasta_parser

UniProt FASTA parser written in pure python.

## Development setup

Create a `venv`:

```sh
python -m venv venv
```

Activate it:

```sh
source venv/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Install the package in editable mode:

```sh
pip install -e .
```

Install `jupiter` playground:

```sh
pip install jupyter
ipython kernel install --user --name=uniprot_fasta_parser
```

## Tutorial on converting FASTA sequences into CSV format

Get the latest FASTA from UniProt SwissProt:

```sh
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
```

The script `upfp-fasta-to-csv` (installed with `upfp`) can be used.

```console
user@host $ upfp-fasta-to-csv -h
usage: upfp-fasta-to-csv [-h] [-g] [-c CHUNK_SIZE] fasta_filepath csv_filepath

positional arguments:
  fasta_filepath        path to the FASTA file
  csv_filepath          path where to store the CSV file

optional arguments:
  -h, --help            show this help message and exit
  -g, --gzipped         flag to indicate whether the FASTA is gzipped.
                        Defaults to False.
  -c CHUNK_SIZE, --chunk_size CHUNK_SIZE
                        size of the chunks us
```

Provide as input the downloaded gzipped FASTA file and convert it to CSV:

```sh
upfp-fasta-to-csv uniprot_sprot.fasta.gz /path/to/file.csv -g
```
