"""
Implementation of the different mutation operators.

BaseMutationOperator is an abstract class that sports the basic methods to perform the bitwise mutation of a bit string,
OnePlusOneMutationOperator is an implementation of the classical (1+1) EA,
FastMutationOperator is an implementation of our operator.

The inheritance scheme is

    BaseMutationOperator
        |- OnePlusOneMutationOperator
        |- FastMutationOperator

and a sample usage is :

    oneplusone = OnePlusOneMutationOperator(n=100)
    fast = FastMutationOperator(n=100, beta=1.5)

"""

from numpy import linspace
from fastga.utils import flip, wrong_param_error
from fastga.sampling import sample, sample_waiting_time


__all__ = ["BaseMutationOperator", "OnePlusOneMutationOperator", "FastMutationOperator"]


class BaseMutationOperator:
    """
    This abstract class holds the common methods that one would expect in a mutation operator.
    It should not be used directly.
    """

    def __init__(self, n): 
        if not isinstance(n, int) or n < 1:
            raise ValueError("Parameter 'n' must be a positive integer. Received {}.".format(n))
        self.n = n

    def get_mutation_rate(self):
        raise NotImplementedError() # this should be implemented in subclasses

    def _mutate(self, bit_string):
        """
        Private 'mutate' method, not to be called externally. Performs an inplace mutation of
        the input bit string. A naive implementation would be to go through the n bits of the
        bit string and flip them with probability given by the mutation rate.
        Alternatively, one can sample the indexes of bits to flip, and flip exactly those. This
        is what we do here.
        """
        n = self.n
        mutation_rate = self.get_mutation_rate()
        index = sample_waiting_time(mutation_rate)
        while index < n:
            flip(bit_string, index)
            index += sample_waiting_time(mutation_rate)

    def mutate(self, bit_string, inplace=False):
        """
        Public 'mutate' method ; can perform the mutation inplace or return a (new)
        mutated bit string.
        """
        n = self.n
        bit_string_len = len(bit_string)
        if not bit_string_len == n:
            raise ValueError("Wrong length for input bit string : expected {}, got {}."
                    .format(n, bit_string_len))
            if not inplace:
                bit_string = bit_string.copy()
        self._mutate(bit_string)
        if not inplace:
            return bit_string


class OnePlusOneMutationOperator(BaseMutationOperator):

    def __init__(self, n):
        super().__init__(n)

    def get_mutation_rate(self):
        return 1 / self.n


class FastMutationOperator(BaseMutationOperator):

    def __init__(self, n, beta):
        super().__init__(n)
        if beta <= 1:
            raise ValueError("Wrong value for parameter beta : received {}, must be a float > 1."
                    .format(beta))
            self.beta = beta
        # We pre-compute the power law cumulative distribution function with the given parameter
        # beta. It will allow us to sample random integers according to this distribution.
        power_law = (linspace(1, n//2, n//2) ** (- beta)).cumsum()
        power_law /= power_law[-1]
        self.power_law = power_law

    def get_mutation_rate(self):
        r = sample(self.power_law)
        return r / self.n


if __name__ == '__main__':
    fast = FastMutationOperator(10, 1.5)
    bit_string = [0] * 10
    print(bit_string)
    for i in range(10):
        fast.mutate(bit_string, inplace=True)
        print(bit_string)

