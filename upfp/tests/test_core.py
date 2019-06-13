"""Tests for the upfp.core submodule."""
import unittest
from upfp.core import FASTA_HEADER_REGEX, parse_fasta
from .utils import TestFileContent


class TestCore(unittest.TestCase):
    """Testing upfp.iterator submodule."""

    def test_fasta_header_regex(self):
        """Test FASTA_HEADER_REGEX."""
        a_header = (
            '>sp|Q91G88|006L_IIV6 Putative KilA-N domain-containing protein '
            '006L OS=Invertebrate iridescent virus 6 OX=176652 GN=IIV6-006L '
            'PE=3 SV=1'
        )
        groups = FASTA_HEADER_REGEX.match(a_header).groups()
        self.assertEqual(
            'sp', groups[0]
        )
        self.assertEqual(
            'Q91G88', groups[1]
        )
        self.assertEqual(
            '006L_IIV6', groups[2]
        )
        self.assertEqual(
            'Putative KilA-N domain-containing protein 006L',
            groups[3]
        )
        self.assertEqual(
            'Invertebrate iridescent virus 6',
            groups[4]
        )
        self.assertEqual(
            '176652',
            groups[5]
        )
        self.assertEqual(
            'IIV6-006L',
            groups[7]
        )
        self.assertEqual(
            '3',
            groups[8]
        )
        self.assertEqual(
            '1',
            groups[9]
        )
        another_header = (
            '>sp|A9CBA2|105R_ADES1 Protein 105R OS=Snake adenovirus '
            'serotype 1 OX=189830 PE=3 SV=1'
        )
        groups = FASTA_HEADER_REGEX.match(another_header).groups()
        self.assertEqual(
            'sp', groups[0]
        )
        self.assertEqual(
            'A9CBA2', groups[1]
        )
        self.assertEqual(
            '105R_ADES1', groups[2]
        )
        self.assertEqual(
            'Protein 105R',
            groups[3]
        )
        self.assertEqual(
            'Snake adenovirus serotype 1',
            groups[4]
        )
        self.assertEqual(
            '189830',
            groups[5]
        )
        self.assertEqual(
            None,
            groups[7]
        )
        self.assertEqual(
            '3',
            groups[8]
        )
        self.assertEqual(
            '1',
            groups[9]
        )

    def test_parse_fasta(self):
        """Test parse_fasta."""
        content = r""">sp|Q6GZX0|005R_FRG3G Uncharacterized protein 005R OS=Frog virus 3 (isolate Goorha) OX=654924 GN=FV3-005R PE=4 SV=1
MQNPLPEVMSPEHDKRTTTPMSKEANKFIRELDKKPGDLAVVSDFVKRNTGKRLPIGKRS
NLYVRICDLSGTIYMGETFILESWEELYLPEPTKMEVLGTLESCCGIPPFPEWIVMVGED
QCVYAYGDEEILLFAYSVKQLVEEGIQETGISYKYPDDISDVDEEVLQQDEEIQKIRKKT
REFVDKDAQEFQDFLNSLDASLLS
>sp|Q91G88|006L_IIV6 Putative KilA-N domain-containing protein 006L OS=Invertebrate iridescent virus 6 OX=176652 GN=IIV6-006L PE=3 SV=1
MDSLNEVCYEQIKGTFYKGLFGDFPLIVDKKTGCFNATKLCVLGGKRFVDWNKTLRSKKL
IQYYETRCDIKTESLLYEIKGDNNDEITKQITGTYLPKEFILDIASWISVEFYDKCNNII
"""
        with TestFileContent(content) as test_file:
            sequences = parse_fasta(test_file.filename, gzipped=False)
            sequence = next(sequences)
            self.assertEqual(
                {
                    'db': 'sp',
                    'accession_number': 'Q6GZX0',
                    'entry_name': '005R_FRG3G',
                    'recommended_name': 'Uncharacterized protein 005R',
                    'organism_name': 'Frog virus 3 (isolate Goorha)',
                    'organism_id': '654924',
                    'gene_name': 'FV3-005R',
                    'protein_existence': '4',
                    'sequence_version': '1',
                    'sequence': (
                        'MQNPLPEVMSPEHDKRTTTPMSKEANKFIRELDKKPGDLAVVSDFVKRNTGKRLPIGKRS'
                        'NLYVRICDLSGTIYMGETFILESWEELYLPEPTKMEVLGTLESCCGIPPFPEWIVMVGED'
                        'QCVYAYGDEEILLFAYSVKQLVEEGIQETGISYKYPDDISDVDEEVLQQDEEIQKIRKKT'
                        'REFVDKDAQEFQDFLNSLDASLLS'
                    )
                },
                sequence
            )
            sequence = next(sequences)
            self.assertEqual(
                {
                    'db': 'sp',
                    'accession_number': 'Q91G88',
                    'entry_name': '006L_IIV6',
                    'recommended_name': 'Putative KilA-N domain-containing protein 006L',
                    'organism_name': 'Invertebrate iridescent virus 6',
                    'organism_id': '176652',
                    'gene_name': 'IIV6-006L',
                    'protein_existence': '3',
                    'sequence_version': '1',
                    'sequence': (
                        'MDSLNEVCYEQIKGTFYKGLFGDFPLIVDKKTGCFNATKLCVLGGKRFVDWNKTLRSKKL'
                        'IQYYETRCDIKTESLLYEIKGDNNDEITKQITGTYLPKEFILDIASWISVEFYDKCNNII'
                    )
                },
                sequence
            )

