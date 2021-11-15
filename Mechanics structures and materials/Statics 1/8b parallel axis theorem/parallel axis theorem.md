---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Parallel axis theorem
An example can be found at [[parallel axis theorem and other example#Using the parallel axis theorem]]
### Equation

> ### $$ I_{z'z'} = I_{zz} + Ab^{2} $$ 
>> where:
>> $I_{z'z'}=$ [[second moment of area]] around z'
>> $I_{zz}=$ [[second moment of area]]
>> $A=$ Area of shape
>> $b=$ Seperation between centre line of shape and [[neutral surface and neutral axis|neutral axis]]

### Setup
Suppose you want to use on of the [[standard results for second moment of area]] for a shape that isn't on the [[neutral surface and neutral axis|neutral axis]]:

![[Pasted image 20211115100244.png]]

But instead has centre:
- $y' = y+b$
- $z' = z+a$

These *parrallel axis* are ment to be used instead, see where this is going?

### Maths
$$\begin{align*}
   I_{z'z'} &= \int \int (y+b)^{2} \cdot dydz\\
&= \int \int   y^{2}+2by+b^{2}   \cdot dydz\\
&= \int \int   y^{2}   \cdot dydz + 2b \int \int  y  \cdot dydz + b^{2}\int \int 1 \cdot dydz\\
& & 0 &= \int \int  y  \cdot dydz& Area &= \int \int 1 \cdot dydz\\
&= \int \int   y^{2}   \cdot dydz + 2b\cdot 0+ b^{2}\cdot A\\
&= \int \int   y^{2}   \cdot dydz + Ab^{2}
\end{align*}$$