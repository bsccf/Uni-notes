---
aliases: ["echelon form"]
tags: ["Question","QFormat3"]
---

#### What is
## Matrix echelon form
This is basically when you do the method from [[using elementary row operations to get the upper-triangular form]] but it resaults in a matrix with rows containing zeros along the diagonal:


### Example
> Get the following matrix into [[matrix echelon form]]:
> $$ \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 3 & 2 \\ 2 & 1 & 5 & 4 \\ 1 & -2 & 0 & 2 \end{pmatrix} $$

$$\begin{align*}
&\begin{pmatrix} 
0 & 1 & 1 & 0 \\ 
1 & 0 & 3 & 2 \\ 
2 & 1 & 5 & 4 \\ 
1 & -2 & 0 & 2 
\end{pmatrix}\\
swap\:1,4&\\
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
2 & 1 & 5 & 4 \\ 
1 & -2 & 0 & 2 \\
0 & 1 & 1 & 0 
\end{pmatrix}\\
(2)-2\tines&\\
&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & -2 & -3 & 0 \\
0 & 1 & 1 & 0 
\end{pmatrix}\\

&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & 0 & -5 & 0 \\
0 & 0 & 2 & 0 
\end{pmatrix}\\

&\begin{pmatrix} 
1 & 0 & 3 & 2 \\ 
0 & 1 & -1 & 0 \\ 
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 
\end{pmatrix}\\

\end{align*}$$