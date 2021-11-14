---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Mesh analysis method
# WRONG, redo from onenote notes
### Method

1) Draw "loop currents" around each loop (these arn't real currents but help with analysis, at any given point the sum of adjacent loop currents will equal the real current). They should all be clockwise.
2) Get equations according to [[Kirchov's voltage law]] around each loop current

### Example
Find expressions for the resistances in this circuit:
![[Pasted image 20211107153425.png]]

1) We draw loop currents.
![[Pasted image 20211113235757.png]]

2) 
> $$ R_1() = V $$
>
> - The sign of the pd of the component is descided by the direction of the pd arrow relative to the current loop arrow.
> - The pd accross the component is worked out using the current on that branch
> - The current on the branch is worked out using the sum of the adjasent loop currents
> 
> We can rewrite the equations into the following form:
> $$
\begin{align*}
V &= I_1 (R_1+R_3) &&+ I_2 (-R_3) &&+ I_3 (-R_1)\\
0 &= I_1 (R_3) &&+ I_2 (R_3-R_2) &&+ I_3 (-R_5-R_2)\\
0 &= I_1 (R_1) &&+ I_2 (R_2) &&+ I_3 (-R_1-R_2-R_4)
\end{align*}$$
> 
> This can then be easily converted into matrix form:
> 
> $$
\begin{align*}
\begin{pmatrix} V \\ 0 \\ 0 \end{pmatrix} &= \begin{pmatrix} (R_1+R_3) &  (-R_3) & (-R_1) \\ (R_3) & (R_3-R_2)  & (-R_5-R_2) \\ (R_1) &  (R_2) & (-R_1-R_2-R_4) \end{pmatrix}\begin{pmatrix} I_1 \\  I_2 \\ I_3 \end{pmatrix}\\
\begin{pmatrix} (R_1+R_3) &  (-R_3) & (-R_1) \\ (R_3) & (R_3-R_2)  & (-R_5-R_2) \\ (R_1) &  (R_2) & (-R_1-R_2-R_4) \end{pmatrix}^{-1}\begin{pmatrix} V \\ 0 \\ 0 \end{pmatrix} &= \begin{pmatrix} I_1 \\  I_2 \\ I_3 \end{pmatrix}
\end{align*}$$
> And done, holy shit that took ages to write out. 