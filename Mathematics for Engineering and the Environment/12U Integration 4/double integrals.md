---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are
## Double integrals
### Theory
Basically so far you have been dealing with single integrals, things that are integrated with respect to one variable, but of course many things have their values depend on multiple input variables so this is where things get difficult... is what I would say if it was, it's actually not that bad, litterally just integrating the normal way twice for 2 speretate variables for example:

$$\begin{align*}
D_{nuts} &= \int \int \int \int f(t,r,o,l)\cdot dt \cdot dr \cdot do \cdot dl & f(t,r,o,l) &= trol^{2} \\
 &= \int \int \int \int trol^{2}\cdot dt \cdot dr \cdot do \cdot dl\\
&= \int \left(\int \left(\int \left(\int t\cdot dt\right)rol^{2} \cdot dr\right) \cdot do\right) \cdot dl\\
&= \int \left(\int \left(\int \left( \frac{t^{2}}{2}+k_{1}\right)rol^{2} \cdot dr\right) \cdot do\right) \cdot dl\\
&= \int \left(\int \left(\int \left( \frac{t^{2}}{2}+k_{1}\right)r \cdot dr\right)ol^{2} \cdot do\right) \cdot dl\\
&= \int \left(\int \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right)ol^{2} \cdot do\right) \cdot dl\\
&= \int \left(\int \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right)o \cdot do\right)l^{2} \cdot dl\\
&= \int \left( \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right) \frac{o^{2}}{2} + k_{3} \right)l^{2} \cdot dl\\
&= \left( \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right) \frac{o^{2}}{2} + k_{3} \right) \frac{l^{3}}{3} + k_{4} \\
\end{align*}$$

My examples kinda cursed but I hope you get the idea, it's just single integration over and over again. The hard part's really just getting the limits right, so yeah, I want to say skill issue but I've overused that now, uuuuh [[git guuuuudd aoifijuwlaoihjflkjawfdlk|get good?]].

This important notation that needs to be learned is that now when defining limits on integrals you need to also note the variable it is assosiated with, as seen in the example below.

### Example
> Given that $y=zB\sin( zx  )$ find an expression for the volume enclosed within $x=0\to1$ and $z=0\to1$:
> ![[Pasted image 20220225212649.png]]
> (the image isn't accurate but I hope you get the idea)

We know that the area of a 3D cube is $V=xyz$, and that over small differences in x and z you can take y as constant so: $dV = y\cdot dz \cdot dx$, that equation will be our starting point. 

$$\begin{align*}
dV &= y \cdot dz \cdot dx \\
\int^{V}_{0} 1\cdot dV &= \int^{x=1}_{x=0} \int^{z=0}_{z=1} y \cdot dz \cdot dx \\
V &= \int^{x=1}_{x=0} \left(\int^{z=0}_{z=1} zB\sin( zx  ) \cdot dz\right) \cdot dx \\
&= B\int^{x=1}_{x=0} \left[ -\frac{z\cos(xz)}{x} + \sin\frac{xz}{}  \right]^{z=0}_{z=1} \cdot dx \\
\end{align*}$$

[[integration]]