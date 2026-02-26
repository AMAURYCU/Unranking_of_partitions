# Unranking of partitions

This project accompanies the paper *Lexicographic Unranking Algorithms for the Twentyfold Way* (https://cnrs.hal.science/LIP6/hal-05486059v1).  
It provides implementations of lexicographic unranking algorithms for the problems of the Twentyfold Way related to set partitions.  

This project is composed of one folder per problem, each containing 5 Python files:  
- `combinatorial.py` contains the unranking algorithm for the order induced by the combinatorial interpretation of the counting formula for the problem.  
- `lexicographic.py` contains the unranking algorithm for the lexicographic order as defined in the paper and implemented in the file `lex_order.py`.  
- `example.py` contains an example of the use of the unranking algorithms for random generation and exhaustive generation of the objects of the problem.  
- `test.py` contains exhaustive tests of the unranking algorithms for small values of the parameters of the problem.  
- `values.py` contains the counting formulas for the problems. 
In addition, extra files are provided for other unranking algorithms that are neither in lexicographic order nor in the order induced by the combinatorial interpretation of the counting formula for the problem when it's useful.
