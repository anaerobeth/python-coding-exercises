# Bigram counter using Map-Reduce
import multiprocessing
import string

from map_reduce import MapReduce

def extract_ngrams(filename, ngram_length=2):
    """Read a file and return a sequence of (ngrams, frequency) values
    """
    punctuations = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    print(multiprocessing.current_process().name, 'reading', filename)
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            line = line.translate(punctuations)
            words = line.split()
            try:
                if ngram_length == 2:
                    ngrams = ['{}_{}'.format(words[i-1], words[i]) for i in range(1,len(words))]
            except:
                print('Invalid input')
            for ngram in ngrams:
                output.append( (ngram.lower(), 1) )
    return output


def count_ngrams(item):
    """
    :param item: partitioned data with bigram and a list of its occurrence
    :return: tuple containing the bigram and its frequency
    """
    word, freq = item
    return (word, sum(freq))

def print_results(counts):
    top = counts[:10]
    longest = max(len(word) for word, count in top)
    for word, count in top:
        print('{}: {}'.format(word, count))


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('text/*.txt')

    mapper = MapReduce(extract_ngrams, count_ngrams)
    bigram_counts = mapper(input_files)
    bigram_counts.sort(key=operator.itemgetter(1))
    bigram_counts.reverse()

    if bigram_counts:
        print('Top 10 bigrams by frequency:')
        print_results(bigram_counts)

    """Results:
    Top 10 bigrams by frequency:
    the_world: 9
    beauty_s: 7
    thou_art: 6
    that_thou: 5
    if_thou: 5
    to_be: 5
    thy_beauty: 4
    ten_times: 3
    in_the: 3
    why_dost: 3
    """

