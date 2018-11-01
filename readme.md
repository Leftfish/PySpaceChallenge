# SpaceChallenge

This is a Python port of my solution prepared originally for the Space Challenge project from Udacity course: Object Oriented Programming in Java. As described by the authors: 

> In this project, you will build a simulation that will help us with our mission to Mars!
> The mission is to send a list of items (Habitats, bunkers, food supplies, and rovers) to Mars, but we need to run some simulations first to pick the correct fleet of rockets.

We simulate behavior of two rocket types according to specs provided in [_specs.txt](_specs.txt). Both types differ in maximum cargo and probability of explosion at launch or at landing. 

The simulated mission to Mars has two phases. Phase 1 is meant to send building equipment and construction material to help build the colony. Phase 2 is meant to send the colony of humans along with some food resources.

The goal is to simulate the total cost of launching payload during both Phases, each time for both types of rockets.

The [SpaceChallenge.py](SpaceChallenge.py) module contains all classes and methods necessary to run the sim. In [Simulate.py](Simulate.py) we run 1000 simulations for each type of rockets and both Phases to compare how cost-effective they are on average.

### Note

This is a training project. The goal was to compare how similar ideas (like class inheritance) can be implemented in Java and in Python 3.


