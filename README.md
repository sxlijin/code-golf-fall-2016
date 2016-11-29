# Code Golf


### Overview
This competition focuses on short and succinct code. 
The challenge is to produce answers to the provided problems with as little code as possible.
Your score for each problem will be the file size of your source code for that problem. Your code will not be run,
nor will it be checked for correctness. We will assume that your code runs and produces the correct output.
However, we will have the 1st, 2nd, and 3rd place contestants run their code live for proof that
it runs and proof that it produces the correct output.

### Submission
You will need to submit the source code for each question, so there will be a total of 6 files to submit.
Make a GitHub repository for these six files, and just copy and paste your repository link [here](https://docs.google.com/a/vanderbilt.edu/forms/d/e/1FAIpQLSfRFw3QpcDT8isA3lH1iNk3xvMhMzqeA6-FPLrShLZVs4VrSg/viewform)
* each file must have the problem number somewhere in its name
* you should only submit your source code files and nothing else
* there should be no dots ("." charachters) in your filename except before the extension
* the file size of your file will be evaluated with the python function [os.path.getzise](https://docs.python.org/2/library/os.path.html?highlight=os.path.getsize#os.path.getsize) on an Ubuntu OS. Make sure this is not problematic for your source code.

#### Sample Valid Filenames:
* prob_1.py
* prob1.py
* 1.java
* jibberish1jibberish.cpp

#### Sample Invalid Filenames:
* i_dont_contain_a_number.py
* x.java
* get.ridOfThatExtraDot.cpp
* .filename.java

### Questions

1. How many years since 0 CE have been prime and a palindrome?
2. Produce this

```
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|_/*\_|
/*_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*/_|_\*
```

3. Print out Vanderbilt's phone number, 1 (615) 322-7311, without using any numbers in your source code
4. Print out all 50 US capital cities in order of their latitude
5. Flatten this array: 

```
[[99, 38, 47, 3, 10], [66, 49, 37, 30, 11, 51, 99, 43, 24], [96, 40, 82, 94, 24, 65, 85], [2, 11, 87, 13, 76, 3], [[73, 31, 74], [7, 18], [57, 65, 87], [68, 49], [1, 81, 96], 1, 55, 38, 21, 96, 3], [[57, 98], [92, 43, 74], [64, 18], [99, 62], [75, 73, 42], 33, 56, 71, 24, 2, 50, 9, 71], [100, 50, 42, 36, 16, 80, 80, 88, 32], [[6, 29, 13], [42, 25], [32, 10], [53, 20, 74, 29], 88, 4, 26, 87, 80, 87], [21, 86, 63, 92, 15], [84, 95, 71, 17, 59, 41, 95, 27, 98, 42, 97, 58, 8], [[83, 70], [40, 2, 93, 70], [72, 71, 95, 83], [58, 45, 25], [99, 98, 99], [84, 26], [5, 21], [89, 16], 46, 26, 64], [21, 22, 89], [64, 79], [86, 43], [90, 65, 94, 19], [4, 6, 72, 25], [60, 41, 33, 28], [93, 11], [30, 27, 13], [24, 32, 64], [75, 62], [79, 17], [52, 18, 15], [66, 90], [38, 33, 89], 95, 92, 28, 89, 58, 48, 98, 54, 69, 21, 76, 17, 39, 47, 71, 5]
```

6. print out, in chronological order, each world series victor's name, then the product of the year and the length of their team name
