This repository holds the code base supporting an article submitted to the [GECCO 2017](http://gecco-2017.sigevo.org/index.html/HomePage "GECCO 2017") conference. Since the article is still being reviewed, the authors' identities [cannot be disclosed](http://gecco-2017.sigevo.org/index.html/Call+for+Papers#Double-Blind_Review_Process) for the moment. They will be as soon as the reviewing process is over. In the meantime, this repository will be maintained actively by the authors, however using an anonymous account.

**fastga** is an extremely small module sporting our so-called *fast mutation operator* (or *heavy-tailed mutation operator*), which is designed to perform bitwise mutation using a power-law-distributed mutation rate. This allows a high number of bits to be flipped in one step with high probability (compared to the classical (1+1) EA for example), which is especially desirable when such long-distance "jumps" are necessary to escape local optima.

Requirements
============

- python3+
- NumPy

Installation
============

In a console, type

    pip install fastga

Usage
=====

Our mutation operator is implemented in the class **FastMutationOperator**, along with the abstract class **BaseMutationOperator** (which you shouldn't use directly but rather subclass to your own classes if needed) and the class **OnePlusOneMutationOperator** (which, as the name suggests, is an implementation of the (1+1) EA). In a python shell, type

    from fastga import FastMutationOperator

Two parameters are required to create an instance :

- an integer **n** which is the size of the bit strings that can be mutated by the operator ;
- a float **beta** > 1 which is the exponent used in the mutation rate power law.

Given these two parameters, the operator's mutation rate *r* is such that, for each *i* in {1 .. n//2}, the probability that *r* is *i/n* is proportional to i^{-beta} (with a suitable normalization factor). As such, lower values of beta tend to favor a higher number of bits flipped in one mutation step.

You can now instantiate an operator :

    operator = FastMutationOperator(n=100, beta=1.5)

and use its **mutate** method to mutate *n*-length bit strings :

    bit_string = [0] * 100
    for i in range(10):
        operator.mutate(bit_string, inplace=True)
        print(bit_string)

