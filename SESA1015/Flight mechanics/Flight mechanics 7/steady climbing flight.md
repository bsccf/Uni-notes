---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you model
## Steady climbing flight

The forces acting on an aircraft in steady climbing flight are shown here:
![[Pasted image 20211124105215.png]]

Where:
- $\theta=$ [[climb angle]]
- $\gamma=$ [[thrust vector angle]]

You can write the equibilbrium equations as:

$$\begin{align*}
  & & L+T\sin \gamma &= W \cos \theta & T\cos\gamma-D&=W\sin\theta\\
\frac{dh}{dt} &= V\sin \theta & & & \frac{T\cos\gamma-D}{W}&=\sin\theta\\
&= V \frac{T\cos\gamma-D}{W}
\end{align*}$$

^ea3763

Note that at a [[thrust vector angle]] of zero, this equation is known as the [[specific excess thrust]]. We can also find the climb angle from [[specific excess thrust]]:

$$\begin{align*}
\frac{dh}{dt} &= V \frac{T\cos\gamma-D}{W} & C_L = \frac{2L}{\rho S V^{2} } & C_D = C_{Do} 
\end{align*}$$