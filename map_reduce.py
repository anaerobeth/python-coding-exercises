# Map-Reduce using multiprocessing
# Adapted from https://pymotw.com/2/multiprocessing/mapreduce.html

import collections
import itertools
import multiprocessing

class MapReduce(object):

    def __init__(self, mapper, reducer, num_workers=None):
        """
        :param mapper: Function that converts input value to (key, value)

        :param reducer: Function that reduces key and values from mapper to final output

        :param num_workers: Number of workers to create in the pool
        """
        self.mapper = mapper
        self.reducer = reducer
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        """Maps values by their key as tuples

        :param mapped_values: tuple of (key, value)
        :return: (key, sequence of values)
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)

        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """
        :param inputs: iterable containing the input data
        :param chunksize: portion of input for each worker
        :return: reduced_values
        """
        map_responses = self.pool.map(self.mapper, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reducer, partitioned_data)
        return reduced_values
