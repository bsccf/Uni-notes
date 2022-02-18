---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Calculating power of an AC circuit
Calculating power is easy for [[direct current|DC]] but the same method won't work for an [[alternating current|AC]] since the current is changing... so lets look at an example:

Given these two circuits:
![[Pasted image 20220218163147.png]]

The DC power is easy enough:
$$\begin{align*}
P &= IV
\end{align*}$$

For AC it's not as simple, if we use the equation $P=\frac{V^{2}}{R}$ to find instantanious power then integrate to find average power that will work. So we will also need [[alternating current#^d2c8ea|this equation]], we can let $\phi=0$ in this case.

$$\begin{align*}
P_{Av} &= \frac{1}{T} \int^{T}_{0} P dt & P &= \frac{v^{2}}{R} & v = V_{p} \cos(\omega t)\\
&= \frac{1}{T} \int^{T}_{0} \frac{v^{2}}{R} dt\\
&= \frac{1}{T} \int^{T}_{0} \frac{(V_{p} \cos(\omega t))^{2}}{R} dt\\
&= \frac{1}{T} \frac{ V_{p}^{2} }{R} \int^{T}_{0} (\cos(\omega t))^{2} dt
&= \frac{1}{T} \frac{ V_{p}^{2} }{R} \left[ \frac{t}{2} + \frac{\sin \omega t}{4\omega} \right]^{T}_{0}\\
&= \frac{1}{T} \frac{ V_{p}^{2} }{R} ( \frac{T}{2} + \frac{\sin \omega T}{4\omega} )
\end{align*}$$

Given that 