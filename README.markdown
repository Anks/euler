My attempts at solving the problems at [Project Euler][1]. I’m thinking
of solving each problem in multiple languages.

  [1]: http://projecteuler.net

### Running the solutions

I’m trying to solve the problems in multiple languages. For Python
files, just run the script file from your shell, or pass it to the
Python interpreter. 

Example: `$ ./1.py` or `$ python 1.py`

Use a similar approach for Ruby solutions you come across.

I’m using [SBCL][] for running Lisp. Emacs wizards will want to use
[SLIME][], and other mortals can run the files using something similar to: 

    $ sbcl
    * (load "1.lisp") ;; should load the file into memory
    * (exercise-1) ;; call the appropriate function (if I forgot to put this line into the script)
    * (quit) ;; to exit the SBCL prompt
    $ 

  [SBCL]: http://www.sbcl.org/
  [SLIME]: http://common-lisp.net/project/slime/

-----------------

Ankit Solanki <http://simulacra.in>
