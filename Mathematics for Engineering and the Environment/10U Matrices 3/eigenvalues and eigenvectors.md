---
aliases: ["eigenvalue","eigenvalues","eigenvector","eigenvectors"]
tags: ["Question","QFormat3"]
---

#### What are
## Eigenvalues and eigenvectors

### Eigenvalues
These are values that induce the equivilent transformation as a specific square matrix for a specific column vector. ($Au=\/lambda$)

The eigenvalues of a [[square matrix]] can be found using:
> ### $$ 0 = \det ( \lambda I - A) $$ 
>> where:
>> $\lambda=$ [[eigenvalues and eigenvectors|eigenvalues]] 
>> $I=$ [[unit matrix]]
>> $A=$ some [[square matrix]]
>> $\det(X)=$ [[determinant]] function

#### Example
> Find the [[eigenvalues and eigenvectors|eigenvalues]] for:
> $$ \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix} $$

$$\begin{align*}
0 & =\det \left( \lambda \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix} \right) \\
&= \det \begin{pmatrix} \lambda+2 & -1 \\ -1 & \lambda+2 \end{pmatrix} \\
&= (\lambda+2)^{2} - 1\\
&= \lambda^{2} + 4\lambda + 3\\
&& \lambda &= -1 & \lambda &= -3
\end{align*}$$

[[eigenvalues and eigenvectors|Eigenvalues]] are -1, -3

### Eigenvectors

