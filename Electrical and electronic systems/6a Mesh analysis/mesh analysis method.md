---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Mesh analysis method

### Method

1) Mark your diagram according to the [[ciruit analysis sign convention]]
2) Draw "loop currents" around each loop (these arn't real currents but help with analysis, at any given point the sum of adjacent loop currents will equal the real current)
3) Get equations according to [[Kirchov's voltage law]]

### Example
Find expressions for the resistances in this circuit:
![[Pasted image 20211107153425.png]]

1) First we mark the diagram according to [[ciruit analysis sign convention]]
![[Pasted image 20211107153334.png]]

2) Then we draw loop currents.
![[Pasted image 20211107153309.png]]

3) Now we can get equations:
> Loop 1
> $$ \begin{align*}
i_1 =& I_1 - I_3\\
i_3 =& I_1 - I_2
\end{align*} $$
> $$ V - R_1(I_1-I_3) - R_3 (I_1-I_2) = 0$$
> 
> Loop 2:
> $$ \begin{align*}
i_2 =& I_2 - I_3\\
i_5 =& I_2
\end{align*} $$
> $$ R_3(I_1-I_2) - R_2(I_2-I_3) - R_5 (I_3) = 0$$
> 
> Loop 3:
> $$ \begin{align*}
i_4 =& I_3
\end{align*} $$
> $$ R_1(I_1-I_3) + R_2(I_2-I_3) - R_4 (I_3) = 0$$
> 
