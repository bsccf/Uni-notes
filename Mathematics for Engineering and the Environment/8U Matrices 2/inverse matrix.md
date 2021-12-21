---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find an
## Inverse matrix

> ### $$ A^{-1} = \frac{1}{|A|} adj\:A $$ 
>> where:
>> $A^{-1}=$ [[inverse matrix]] 
>> $|A|=$ [[determinant]] of A
>> $adj\:A=$ [[adjoint matrix]]
>> $AA^{-1} = I$
>> $I=$ [[unit matrix]]

If you look back at the [[adjoint matrix]] page you can see under it's strange properties how it can easily be manipulated to give an inverse matrix.

### Example
#### 2x2 matrix
> Find the inverse of $A=\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$

$$\begin{align*}
A^{-1}&= \frac{1}{det\:A} adj\:A \\
&= \frac{1}{det\:A} (cofactors\:A)^{T} \\
&= \frac{1}{det\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}} (cofactors\:\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix})^{T}\\
&= \frac{1}{1*3-2*2} (cofactors\:\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix})^{T}
\end{align*}$$
