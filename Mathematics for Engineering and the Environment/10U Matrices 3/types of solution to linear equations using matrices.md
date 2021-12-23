---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we determine the
## Types of solution to linear equations using matrices

![[Pasted image 20211223162423.png]]

If we have a [[matrix in echelon form]] as shown above that is acompanyed by a [[column vector]] containing solutions (here we have it in [[adjoint matrix]] form) then the following rules apply (here this is for solving sets of linear equations):
1) If the rank of the [[augmented matrix]] is greater than the rank of the coefficient matrix the set of linear equations are [[inconsistant equations|inconsistant]].
2) If the ranks of these matrices are equal then the system has one set of solutions and is [[consistant equations|consistant]].
3) If the rank of the coefficient matrix is higher than the [[augmented matrix]] then the equations has infinate solutions and is [[consistant equations|consistant]].

Note that:
Rank of [[augmented matrix]] = $u$
Rank of coefficient matrix = rank of the matrix containing the single numerical equivilences of each equation (not sure if I phrased that well, the skinny matrix that goes on the right, though you will need to go from [[augmented matrix]] back to the origional split form [[augmented matrix#^5130a9|example]])

### Example
> Given the following matrix, determine how many sets of solutions exist.
> $$ \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 3 & 2 \\ 2 & 1 & 5 & 4 \\ 1  & -2 & 0 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix}1 \\ 3 \\ 7 \\ 2\end{pmatrix} $$

(Imagine I have lots of working here (it's the same as [[matrix in echelon form#Example]] but modifieng the coefficient matrix as well during [[elementary row operations with constant solutions|elementary row operations]]))

$$\begin{align*}
 \begin{pmatrix}1 & \frac{1}{2} & \frac{5}{2} & 2 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}\begin{pmatrix}x_1 \\ x_2 \\ x_3 \\ x_4\end{pmatrix} &= \begin{pmatrix} \frac{7}{2} \\ \frac{3}{5} \\ - \frac{1}{5} \\ \frac{2}{5}\end{pmatrix}
\end{align*}$$
The rank of the main matrix is 3 while the coefficient matrix is 4 