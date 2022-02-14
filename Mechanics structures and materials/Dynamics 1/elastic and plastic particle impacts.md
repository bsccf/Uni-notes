---
aliases: ["elastic impact","plastic impact"]
tags: ["Question","QFormat3"]
---

#### What are
## Elastic and plastic particle impacts
### Stuff
Basically take what you learned from [[modeling particle impacts]] more specifically [[coefficient of restitution]] and:
- $e=1$ means [[elastic and plastic particle impacts|elastic impact]]
- $0<e<1$ non elastic impact, some KE lost
- $e=0$ [[elastic and plastic particle impacts|plastic impact]], maximum energy dissipation (lots of KE loss), after the impact the particles stick together moving off with a single velocity

Heres the slide on how to solve these if you haven't figured it out already:
![[Pasted image 20220214120757.png]]

### Example
> Given the following situation:
> ![[Pasted image 20220214122237.png]]
> If balls a and b are the same density and $e$ is known and equal for all collisions write an expression for the max height A reaches, modelling both as particles. A is the smaller ball.

First we need an expression for velocity at the instant of impact with the ground as well as expressions for the mass of A and B:
$$\begin{align*}
v_{0} &= Hg & m_{A} &=  \frac{4\rho \pi r^{3}}{3} & m_{B} &=  \frac{4\rho \pi (kr)^{3}}{3}\\
\end{align*}$$

Now we find the momentum of B after it's impact with the ground:
$$\begin{align*}
e(m_{B}v_{0}) &= -m_{B}v_{0}
\end{align*}$$