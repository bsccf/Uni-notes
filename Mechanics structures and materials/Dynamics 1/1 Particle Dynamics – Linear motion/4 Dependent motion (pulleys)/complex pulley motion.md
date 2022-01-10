---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Complex pulley motion
Ok so this is actually really cool, most effective to explain with a diagram:
![[Pasted image 20220110212319.png]]
Think about the relationship between $s_{A}$ and $s_{B}$, you may think initially that it's the same as what we covered in [[basic pulley motion]] but look at the diagram and picture what happens... the motion of $\Delta s_{B} = \frac{1}{2} \Delta s_{A}$, this comes because we have a different equation govening the cord length distrobution:

> ### $$ 2s_{B} + s_{A} + h  = l_{T} $$ 
>> where:
>> $l_{T}=$ total cord length 
>> $l_{CD}=$ cord length over pully (sometimes approximated to zero)
>> $s_{A},s_{B}=$ cords on each side of the pully

Which is distincly different to the [[basic pulley motion#^f9b477|simular equation taken from basic pully motion]].
We can apply the same differentiation process:
$$\begin{align*}
2s_{B} + s_{A} + h  &= l_{T}\\
2 \frac{ds_{B}}{dt} + \frac{ds_{A}}{dt} &= 0\\
\frac{ds_{B}}{dt} &= - \frac{1}{2} \frac{ds_{A}}{dt}\\

\Delta s_{B} &= \frac{1}{2} \Delta s_{A}
\end{align*}$$