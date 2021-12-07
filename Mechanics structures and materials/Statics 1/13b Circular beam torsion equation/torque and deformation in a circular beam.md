---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the relationship between
## Torque and deformation in a circular beam


### Proof
We know that torque is just a moment acting around the midpoint:
![[Pasted image 20211207132036.png]]

If we take a slice as shown above, then find the force acting over a small distance and multiply it by the distance from where we are taking moments about (the centre) we can find the moment that counteracts the torque.
This force that is acting over the small distance can be expressed using the known [[shear stress in a circular beam (torsion)|stress that acts here]].

So we can get an expression for the force acting on this small section in a ring at distance r:

$$\begin{align*}
dF &= \tau (r\times d\psi \times dr)
\end{align*}$$
Since it's a small area we can multiply it by its distance to get the torque it resaults in:
$$\begin{align*}
dT &= r\times dF \\
&= r^{2}\times  \tau \times d\psi \times dr
\end{align*}$$

![[Pasted image 20211207133148.png]]

We also know that the total torque is the sum of all these tiny rings along the beams radius, hence:
$$\begin{align*}
T &= \int^{R}_0 \int^{2\pi}_0 r^{2}  \tau \cdot d\psi \cdot dr\\
T &= \tau\int^{R}_0 [ r^{2}   \psi]^{2\pi}_0 \cdot dr\\
T &= \tau \int^{R}_0 r^{2}  2\pi \cdot dr\\
T &= 2\pi\tau \left[ \frac{r^{3}}{3}  \right]^{R}_0 \\
T &=\frac{2\pi R^{3} \tau }{3} \\
&
\end{align*}$$