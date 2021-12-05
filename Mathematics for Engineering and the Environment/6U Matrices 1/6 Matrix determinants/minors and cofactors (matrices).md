---
aliases: ["cofactor","minor"]
tags: ["Question","QFormat3"]
---

#### What is a
## Minors and cofactors (matrices)
### Minors
If we take the following 3x3:
$$\begin{align*}
B &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}
\end{align*}$$

The minor at position $a_{ij}$ can be found by crossing out the row $i$ and column $j$ then [[finding the determinant of a 2x2 matrix|finding the determinant of the remaining 2x2]]. 
#### Example for $a_{11}$:

$$\begin{align*}
B &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}\\
minor_{11} &= \begin{pmatrix} a_{11} &  a_{12} &  a_{13} \\  a_{21} &  a_{22} &  a_{23} \\  a_{31} &  a_{32} &  a_{33} \end{pmatrix}
\end{align*}$$
