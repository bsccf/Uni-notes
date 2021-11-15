---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Parallel axis theorem
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
&= \int \int   y^{2}   \cdot dydz + 2b \int \int  y  \cdot dydz + b^{2}\int \int 1 \cdot dydz
\end{align*}$$