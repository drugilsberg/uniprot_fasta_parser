[![Build Status](https://travis-ci.org/drugilsberg/uniprot_fasta_parser.svg?branch=master)](https://travis-ci.org/drugilsberg/uniprot_fasta_parser)
# uniprot_fasta_parser

UniProt FASTA parser written in pure python.

## Setup the environment

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
ipython kernel install --user --name=repo-name
```

## Get FASTA from UniProt

```sh
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
```
