import cupy as cp

class root_finders():

    def __init__(self):
        pass

    def bisection(self, fn,x0,x1,e):
        """
        Bisection Method for finding real root of nonlinear 
        equation in python programming language.
        In this python program, x0 and x1 are two initial guesses, 
        e is tolerable error and nonlinear function f(x) is defined 
        using python function definition.

        Algorithm:

        1. start

        2. Define function f(x)

        3. Choose initial guesses x0 and x1 such that f(x0)f(x1) < 0

        4. Choose pre-specified tolerable error e.

        5. Calculate new approximated root as x2 = (x0 + x1)/2

        6. Calculate f(x0)f(x2)
            a. if f(x0)f(x2) < 0 then x0 = x0 and x1 = x2
            b. if f(x0)f(x2) > 0 then x0 = x2 and x1 = x1
            c. if f(x0)f(x2) = 0 then goto (8)
            
        7. if |f(x2)| > e then goto (5) otherwise goto (8)

        8. Display x2 as root.

        9. Stop
        """
        step = 1

        condition = True
        while condition:
            x2 = (x0 + x1)/2
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, fn(x2)))

            if fn(x0) * fn(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            
            step = step + 1
            condition = abs(fn(x2)) > e

        print('\nRequired Root is : %0.8f' % x2)

    def newton_raphson(self,fn,d_fn,x0,e,N):
        """
        Newton Raphson method for finding real root of nonlinear function in python
        programming language.
        x0 is initial guess, e 
        is tolerable error, fn(x) is non-linear function whose 
        root is being obtained using Newton Raphson method.
        1. Start

        2. Define function as fn(x)

        3. Define first derivative of fn(x) as d_fn(x)

        4. Input initial guess (x0), tolerable error (e) 
        and maximum iteration (N)

        5. Initialize iteration counter i = 1

        6. If d_fn(x0) = 0 then print "Mathematical Error" 
        and goto (12) otherwise goto (7) 

        7. Calcualte x1 = x0 - fn(x0) / d_fn(x0)

        8. Increment iteration counter i = i + 1

        9. If i >= N then print "Not Convergent" 
        and goto (12) otherwise goto (10) 

        10. If |fn(x1)| > e then set x0 = x1 
            and goto (6) otherwise goto (11)

        11. Print root as x1

        12. Stop
        """
        
        step = 1
        flag = 1
        condition = True
        while condition:
            if d_fn(x0) == 0.0:
                print('Divide by zero error!')
                break
            
            x1 = x0 - fn(x0)/d_fn(x0)
            print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, fn(x1)))
            x0 = x1
            step = step + 1
            
            if step > N:
                flag = 0
                break
            
            condition = abs(fn(x1)) > e
        
        if flag==1:
            print('\nRequired root is: %0.8f' % x1)
        else:
            print('\nNot Convergent.')