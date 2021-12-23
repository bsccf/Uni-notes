---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Solving linear equations with non square matricies
Instantly you can tell that using [[inverse matrix|inverse matricies]] aint gunna work ([[if not what have I been teaching you|atleast I hope you realize that]]).

So instead we now make use of all those juicy [[elementary row operations with constant solutions|elementary row operations]], [[I am being forced to say this against my will|exciting]]!

### Example
> Solve: 
> $$ \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}1 \\ 2\end{pmatrix} $$


The elimination is going to take a while, keep up:
#### The elimination
We first subract row 1 from row 2:
$$\begin{align*}
\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix} 
\end{align*}$$

#### Next bit
Now we can expand out our matrix into an equation form:
$$\begin{align*}
\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} &= \begin{pmatrix}1 \\ 2\end{pmatrix}\\
&& x+y+z &= 1 & y+2z &= 2
\end{align*}$$