---
aliases: ["maxamising aircraft range"]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Maximising the breguet range
### Introduction
We know that the [[Breguet range equation]] allows us to calculate aircraft range, but we can use maths to find how to get a maximum value for a given fuel load.

### Math time
![[Breguet range equation#^20c05c]]

So to maxamise range we need to maxamise $\frac{VL}{D}$, so lets start by getting an equation interms of that.

We know $T/\sigma=k$ from [[jet thrust variation in the stratosphere]]:

$$\begin{align*}
   T = D &= \frac{1}{2}\rho V^{2} S C_D\\
&  & T&=k\sigma & \rho&=\rho_0 \sigma\\
k\sigma &= \frac{1}{2}( \rho_0 \sigma ) V^{2} S C_D\\
\frac{2k}{S\rho_0 }  &=V^{2} C_D\\
\therefore V^{2}C_D&=constant\\
 \therefore V&\propto \frac{1}{\sqrt{C_D}} & \frac{C_L}{C_D}&=1 \\
\therefore \frac{VL}{D} &\propto \frac{1}{\sqrt{C_D}} \frac{C_L}{C_D} \\
\end{align*}$$

Now to find the value of $C_L$ that achieves max range we need to differentiate $\frac{1}{\sqrt{C_D}} \frac{C_L}{C_D}$ with respect to $C_L$, then make that equal 0 to get the turning point.
(if you have been paying attention $C_D$ is a function of $C_L$ so this is about to become a [[hahaha I am in pain|shitstorm]].

