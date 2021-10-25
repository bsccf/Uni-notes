---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you get the
## Proof of the differential relationship between load, shear force and bending moment

If we take the following diagram:

![[Pasted image 20211025164706.png]]

Then try to analyse it using [[method for constructing shear force and bending moment diagrams|method for evaluating shear force and bending moment diagrams]]:

We can get a diagram for a beam segment

![[Pasted image 20211025164816.png]]

Vertical equalibrium:
$$\begin{align*}
Q &= Q+dQ + dx\cdot w(x)\\
dQ &= -dx\cdot w(x)\\
\frac{dQ}{dx}&= -w(x)
\end{align*}$$
Here we can approximate the load as $dx\cdot w(x)$ because $dx$ is very small.

Prooving the equation:

> $$ \frac{dQ}{dx} = -w(x) $$ 
>> where:
>> $Q=$ The [[moment on a beam|moment on the beam]]
>> $x=$ the position along the beam
>> $w(x)=$ A function representing the load at a given point

If we also take the moment equalibrium:
$$\begin{align*}
M + (Q+dQ)\cdot dx +  &= M+dM\\
 (Q+dQ)\cdot dx &= dM\\
\end{align*}$$