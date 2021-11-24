---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are the
## Forces acting during take off

![[Pasted image 20211124134849.png]]
![[Pasted image 20211124132645.png]]

We can use these forces to find the acceleration of the aircraft and it's velocity over the length of the runway:

$$\begin{align*}
   (T-D) - \mu(W-L) &= m \frac{dV}{dt} & \frac{W}{g} &= m \\
(T-D) - \mu(W-L) &= \frac{W}{g} \frac{dV}{dt} \\
\frac{T}{W} - \frac{D}{W} - \mu\frac{W-L}{W} &= \frac{1}{g} \frac{dV}{dt} & & & V\frac{dV}{dx} &= \frac{dV}{dt}\\
\frac{T}{W} - \frac{D}{W} - \mu\left(1-\frac{L}{W}\right) &= \frac{V}{g} \frac{dV}{dx}
\end{align*}$$

To find the take off distance to reach the [[screen speed]] the values of L and D must be substituted in the equation of motion which must then be integrated from 0 to [[screen speed]]. An approximate estimate of the distance can be found by making the following assumptions:
- $\frac{T}{W}=constant$, this is basically true since total fuel loss is usually minimal and thrust is roughly constant
- $\frac{D}{W} \approx 0$ and $\frac{L}{W} \approx 0$, this works since the relative values of $L,D$ are small compared to $W$ prior to lift off.

Using these assumptions on the previous equation:
$$\begin{align*}
\frac{T}{W} -0+ \mu\left(1-0\right) &= \frac{V}{g} \frac{dV}{dx}\\
\frac{T}{W} + \mu &= \frac{V}{g} \frac{dV}{dx}\\
\int^{s_1}_0 \frac{T}{W} + \mu\cdot dx&= \int^{V_2}_0 \frac{V}{g} \cdot dV\\
\left[x \frac{T}{W} + \mu x\right]^{s_1}_0 &=  \frac{V^{2}}{2g} 
\end{align*}$$