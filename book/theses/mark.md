# Mark: Expanding the implementation of Macaulay’s method in Python

> The method of Macaulay is a method to determine force and deflection properties of structures. The method makes it possible to describe discontinuous beams with a single equation. The fact that the entire beam can be described in a single equation makes this method well-suited for use in programming. In past Bachelor End Projects students from the TU Delft have made advancements in the application of the method of Macaulay, making it able do be used for more complicated structures.
> 
> SymPy is a Python library that has a Beam module that specialises in calculations of beams. In this module the method of Macaulay is used for some of these calculations. The goal of this project is to use the advancements made by previous Bachelor End Projects to extend the implementation of Macaulay’s method
in SymPy.
> 
> This leads to the following research question: How can the current implementation of Macaulay’s method be extended in Python to be able to calculate and analyze more complicated beams and structures, based on the advancement made by previous Bachelor End Projects at the TU Delft?
>
> The advancements made by previous Bachelor End Projects can be divided up into different subjects. These subjects can be implemented one by one. During the course of the project there has been focus on implementing two of these subjects. The first subject is rotation and sliding hinges. The second subject is calculations of influence line diagrams. Both these subjects are completely implemented into the SymPy code.
> In the implementation of rotation and sliding hinges, the mechanics calculation done by the SymPy code are changed. These hinges are now directly added to the load equation of the beam using singularity functions. The main advantage of this is that calculations on beams with hinges can be done on the beam as a whole, instead of having to cut the beam up into different parts. The fact that the beam can be calculated as a whole also makes this method able to be scaled to calculate beams with multiple hinges.
>
> There was already an existing implementation to calculate influence line diagrams, but this implementation could be improved. In the new implementation the moving load is added to the load equation using a singularity function. The ability to apply the boundary conditions that come with hinges is also added in the new implementation. This makes the new implementation able to calculate correct influence lines for beams with and without hinges.
>
> There are more advancements made by previous Bachelor End Projects than implemented during this project. The advancements on some other subjects, for example normal forces or spring connections, can still be implemented into the current Beam module. For other advancements, those regarding 2D structures, it will be better if they are implemented in a new module. This new module could specialize in 2D structures, while the current module stays focused on calculations on single beams.
>
> In the end it can be concluded that the implementation of Macaulay’s method can be extended in Python by first taking a look at the mechanics calculations. In these calculations the method of Macaulay should be used in the most optimal way. After changing these calculations, the software design can be adjusted to be able to make these calculations. With the implementation of these new mechanics calculations the software can calculate and analyse more complicated beams and structures.

## Documenten
- [TU Delft Education repository](http://resolver.tudelft.nl/uuid:96ec934a-4520-465f-8079-01b9fad73360)
- [GitHub repository old code](https://github.com/mvg2002/BEP_examples_SymPy_1.12), also shown in this book
- [GitHub repository new code](https://github.com/mvg2002/BEP_examples_SymPy_1.14.dev), also shown in this book
- [GitHub respoitory other example](https://github.com/mvg2002/Beam-examples), also shown in this book