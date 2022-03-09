---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Couette flow for a newtonian fluid
Using the theory from [[newtonian fluids]] and applying it to [[couette flow]] we can demonstrate it's application under a simple situation:
![[Pasted image 20220309213243.png]]
So the top plate is moving with a velocity $V_{0}$ and the bottom is stationary, if we take the [[fluid no slip condition]] into account then we know that a very thin layer adjastent to both the top and bottom layers is moving with the same velocity it's got. So lets turn these ideas into math:
$$\begin{align*}
at\: t&=0 & at\:t&=0 \\
x&=0 & at\:x&=D\\
V &= V_{0}  & V&=0
\end{align*}$$
Where $V$ is the velocity of a thin layer of fluid and $x$ is distance normal to the top layer.
We can take fluid layer thickness as thin $(dx)$ and the difference in velocity between adjasent layers as $dV$, the change in velocity will be proportional to the change in shear force $d\tau$ since net force on the layer will be the resault of the sum of the acceleration force from the top layer and the [[I used it in the right context so I can not be critisized fucking owned|retarding]] force from the bottom layer:
$$\begin{align*}
A d\tau &= dV \cdot dm & dm &= \rho (A \cdot dx)\\
d\tau &= dV \rho \cdot dx
\end{align*}$$
Now if we take the equation from [[newtonian fluids#^998109]] we can do some maeth:
$$\begin{align*}
\tau = \mu \times dV
\end{align*}$$