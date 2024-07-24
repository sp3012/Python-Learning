****************** LOOP **********************

1. FOR LOOP 

--> Iterabales: lists, tuples, strings, dictionaries, sets and range.

--> Definition: An iterable is an object that implements the __iter__() method, which returns an iterator, or it must implement the __getitem__() method to support indexed access.

Iterator: An iterator is an object that implements the __next__() method, which returns the next item from the sequence and raises StopIteration when there are no more items.

--> for loop by default provides the elements of the iterable

--> range() generates index values: When you use range() in a for loop, it produces a sequence of numbers, which are typically used as indices.

--> Loop Control
    break: Exit the loop prematurely.
    continue: Skip the current iteration and continue with the next.
    else: Optional block executed if the loop completes normally (i.e., no break).

--> enumerate(): To get index and value while iterating:
--> zip(): To iterate over multiple iterables in parallel:

---------- LOOP on DICTIONERIES ----------

FOR KEY
for key in my_dict.keys()

FOR VALUE: 
for value in my_dict.values()

FOR KEY AND VALUES BOTH
for key, value in my_dict.items()




1. What is the purpose of the else clause in a loop? Provide an example.
Ans. The else clause in a loop serves a specific purpose: it executes a block of code after the loop completes its iterations normally, without being interrupted by a break statement. If the loop is terminated prematurely by a break statement, the else clause is not executed.

2. Explain the use of enumerate in loops. Provide an example.
Ans. enumerate() in Python provides index-value pairs for iterating over a sequence(list, dictionary, tuples, string){iterable objects}

3. How can you iterate over multiple lists simultaneously using a loop
Ans. To iterate over multiple lists simultaneously in Python, you can use the zip() function along with a loop. The zip() function takes multiple iterables (like lists) and returns an iterator that produces tuples containing elements from each iterable.
NOTE: Make sure that the lists you pass to zip() are of the same length. If they are not of the same length, zip() will stop iterating as soon as the shortest iterable is exhausted.

4. How does Python's for loop differ from traditional for loops in other programming languages?
Ans. Python’s for Loop:
Acts like a foreach loop.
Iterates over elements of a sequence.
No explicit index variable needed.
Directly represents each element.
Readable and concise.

*** Difference between range and slicing:
Slicing ([]): Extracts values from a sequence based on indices, returning a subsequence.
range() Function: Generates a sequence of integers, often used for looping or indexing purposes.

They are both fundamental tools in Python for manipulating and accessing sequences, but they serve distinct purposes: slicing for extracting values from sequences and range() for generating sequences of numbers.
