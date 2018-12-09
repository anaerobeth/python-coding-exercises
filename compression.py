"""Compress DNA Sequences

Adapted from: Classic Computer Science Problems in Python
Encode ATGC char as bit string (2 bits) instead of str (8 bits)
Mapping: A = 00, T = 11, G = 10, C = 01
Tip: sys.getsizeof() to get memory size of Python objects

Convert
Map each char to bit string then return array of ints
f(g) := { m = {'A': 0b00, 'T': 0b11, 'G': 0b10, 'C': 0b01 };
    [ m[c] for c in g]  }

Compress
For each char, shift 2 bits to the left then add mapped suffix using OR
f(g) := { bs = 1; (bs <<= 2, bs |= m[c] for c in g) }

Decompress
Read compressed string 2 bits at a time but exclude the sentinel,
Add char mappings to build a string then return the reversed string
f(cg) := { g = ''; b = bs >> i, g += rev_m[b] for i in range(0, bs.bit_length()-1, 2); rev(g) }

>>> CompressedGene('ATG')._convert()
[0, 3, 2]
>>> CompressedGene('ATG')._compress()
78
>>> print(CompressedGene("TAGGGATTAACCGTTATATATATATAGCCATGG"))
TAGGGATTAACCGTTATATATATATAGCCATGG
"""


class CompressedGene:
    def __init__(self, gene):
        for char in gene:
            if char not in ['A', 'T', 'G', 'C']:
                raise ValueError('Invalid input')
        self.m = {'A': 0b00, 'T': 0b11, 'G': 0b10, 'C': 0b01 }
        self.rev_m = dict(map(reversed, self.m.items()))
        # => {0: 'A', 3: 'T', 2: 'G', 1: 'C'}
        # OR dict(zip(self.m.values(),self.m.keys()))
        # OR {k:v for k, v in self.m.items() if v == 1}
        self.gene = gene.upper()
        self._compress()


    def _convert(self):
        return [ self.m[char] for char in self.gene]


    def _compress(self):
        self.bit_string = 1 # sentinel
        for char in self.gene:
            self.bit_string <<= 2
            self.bit_string |= self.m[char]

        return self.bit_string


    def _decompress(self):
        gene = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11
            gene += self.rev_m[bits]

        return gene[::-1]


    def __str__(self):
        return self._decompress()


if __name__ == '__main__':
    import doctest
    from sys import getsizeof
    doctest.testmod()

    original = "TAGGGATTAACCGTTATATATATATAGCCATGG" * 10
    print("Original is {} bytes".format(getsizeof(original)))

    compressed = CompressedGene(original)
    print("Compressed is {} bytes".format(getsizeof(compressed)))

    print(compressed)
    decompressed = compressed._decompress()
    print("Original and decompressed sequences are the same: {}".format(original == decompressed))
