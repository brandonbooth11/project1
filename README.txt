1. Purpose/description

My program is made to do the goals of project 1, or to implement a Radix sort method on [35, 53, 55, 33,52, 32, 25]
and to implement a method that interprets expressions given in postfix notation and solves them.

My program implements a recursive radix sort algorithm that sorts by the first integer of each number (starting on
the right) and continues sorting digit by digit all the way until it has sorted by the leftmost digit and then it 
stops and returns the fully sorted list. It does this using an array of 10 ArrayQueues, the class for which I pulled
from the blackboard lecture notes.

I solved the postfix problem by reading the expression from left to right and for each character, if it was a number
I put it into an ArrayStack, the class for which I pulled from the blackboard lecture notes, and if it was an 
operation, I took the last 2 digits from the stack and did that operation on them.

2. Installation

Download the project 1 zip file and decompress it. Make sure you have python 3 installed on your computer. Right click
on the Project1.py file and click "edit with IDLE" and then select the version of IDLE that corresponds to the version
of python that you have installed on your pc. Once IDLE is opened, you'll see the code. You can push f5 to run the 
code, or you can go to the bottom of the document and change whatever you like and add new examples or tests for my
methods to work on and then run it to test the program.


** There is no Example usage, dev environment, change log, or any way to contribute to my program, sorry **


7. License and Author Info

The classes of ArrayQueue and ArrayStack used in radixSort and postFix respectively were both pulled from the csc310
blackboard lecture notes for use in this program. The radixSort and postFix functions, however, were original and 
made by Brandon Booth. For any further information or questions, contact me at brandon_booth11@mymail.eku.edu