---
aliases: ["superposition method"]
tags: ["Question","QFormat3"]
---

#### How
## Solving statically indeterminate beams with superposition method
Essentially what this involves is using [[deflection of beams standard resaults]] for [[solving statically indeterminate beams]], by supperimposing standard resaults to get the overall deflection and skip a few steps.

### Example

![[Pasted image 20211129132209.png]]

We just need to superimose [[deflection of beams standard resaults#Uniformly distrobuted load]] and [[deflection of beams standard resaults#Point load]] after rearranging them into the correct format:
(notice that $+\frac{1}{3} \frac{FL^{3}}{EI}$ became $-\frac{1}{3} \frac{FL^{3}}{EI}$, this is because the F direction is reversed)
$$\begin{align*}
   v(L) &= \frac{1}{8} \frac{wL^{4}}{EI} - \frac{1}{3} \frac{FL^{3}}{EI} 
\end{align*}$$
