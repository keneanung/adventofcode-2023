# Problem description

The given problem can be represented as a function with the overall form of $l=tx-x^2$ where `t` is the time of the race and `l` is the distance the boat travels:

Common Formula: $$y = ax^2+bx+c$$
Insert 3 Points: $(0,0), (1,6), (2,10)$ and solve: 
```math
0=a0+b0+c

0=c

6=a+b  | -a

b=6-a

10=4a+2b

10=4a+2(6-a)

10=4a+12-2a | -12

-2=2a | /2

a=-1

b=6-(-1)

b=7
```

So to solve any of the solutions, we have to calculate $l_{Race} < t_{Race} x-x^2$.

For the first example, this term holds true for the integer values of `2, 3, 4, 5`. This puzzle was solved manually by me.
