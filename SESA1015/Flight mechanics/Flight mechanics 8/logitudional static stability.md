---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe and explain
## Logitudional static stability
### Intro

This is where you get [[static stability]] in the pitch axis of the aircraft, expressed mathamatically:

$$\begin{align*}
\frac{dC_{mG}}{d\alpha} &< 0 
\end{align*}$$
$dC_{mG}$ being the pitching moment about the centre of gravity
$\alpha$ being the [[Angle of attack]]

So to calculate this we will need an expression for $C_{mG}$ interms of $\alpha$. Introducing "maths":

### Maths
We will use the following diagram:

![[aircraft controls and dimentions for calculating longitudional stability#^267a4d]]

Now if we take moments about the centre of gravity:
$$\begin{align*}
 M_G &=  M_0 + L_W(h-h_0)c - P( l_T - (h-h_0)c )
\end{align*}$$
Here the $M_0 + L_W(h-h_0)c$ is from the wing and $- P( l_T - (h-h_0)c )$ is from the tailplane.

#### Desired diagram
So we can see by the equation that $P(...)$ is counteracting $L_W(...)$, which is desireable for static stability. But the important bit is how they change with changing $\alpha$ (angle of attack), to get an automatic return to the correct $\alpha$ we will need:
- $M_G<0$ when pitched upward
- $M_G>0$ when pitched downward

![[Pasted image 20211206142406.png]]