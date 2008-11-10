(defun divisible-by (number divisor) 
  (= 0 (mod number divisor)))

(defun divisible-by-3-or-5 (number) 
  (or (divisible-by number 3) (divisible-by number 5)))

(defun exercise-1 ()  
  (reduce '+ 
          (remove-if-not 
           'divisible-by-3-or-5
           (loop for i from 1 to 999 collect i))))

(print (exercise-1))