This repository holds the code base supporting the article "Fast genetic  algorithms" by Benjamin Doerr, Huu Phuoc Le, Régis Makhmara, and Ta Duy  Nguyen. The conference version of this work is accepted for publication in the proceedings of GECCO 2017. An extended version can be found on the ArXiV at https://arxiv.org/abs/1703.03334.

**fastga** is an extremely small module sporting our so-called *fast mutation operator* (or *heavy-tailed mutation operator*), which is designed to perform bitwise mutation using a power-law-distributed mutation rate. This allows a high number of bits to be flipped in one step with high probability (compared to the classical (1+1) EA for example), which is especially desirable when such long-distance "jumps" are necessary to escape local optima.

Requirements
============

- python3+
- NumPy

Installation
============

The pip way (recommended)
-------------------------

**(Optionnal)** Create a python virtual environment and activate it. In a console, type :

::

    $ virtualenv ~/some_convenient_location/fastga
    $ cd ~/some_convenient_location/fastga
    $ source bin/activate

In a console (with your virtualenv activated if you use one), type :

::

    $ pip install fastga

The git way
-----------

Simply clone this repository to a convenient location :

::

    $ mkdir some_convenient_location && cd some_convenient_location
    $ git clone https://github.com/FastGA/fast-genetic-algorithms.git

then add it to your **PYTHONPATH** :

::

    $ export PYTHONPATH=some_convenient_location:$PYTHONPATH

(you can also put this command in your .bashrc file to make it permanent).

Usage
=====

Our mutation operator is implemented in the class ``FastMutationOperator``, along with the abstract class ``BaseMutationOperator`` (which you shouldn't use directly but rather subclass to your own classes if needed) and the class ``OnePlusOneMutationOperator`` (which, as the name suggests, is an implementation of the (1+1) EA). In a python shell, type

::

    from fastga import FastMutationOperator

Two parameters are required to create an instance :

- an integer ``n`` which is the size of the bit strings that can be mutated by the operator ;
- a float ``beta`` > 1 which is the exponent used in the mutation rate power law.

Given these two parameters, the operator's mutation rate *r* is such that, for each *i* in {1 .. n//2}, the probability that *r* is *i/n* is proportional to i^{-beta} (with a suitable normalization factor). As such, lower values of beta tend to favor a higher number of bits flipped in one mutation step.

You can now instantiate an operator :

::

    operator = FastMutationOperator(n=100, beta=1.5)

and use its ``mutate`` method to mutate *n*-length bit strings :

::

    bit_string = [0] * 100
    for i in range(10):
        operator.mutate(bit_string, inplace=True)
        print(bit_string)
