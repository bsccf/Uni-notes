---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Cruise climb technique for a jet
#### Introduction
So we already know [[cruise pattern|the problem]] that [[cruise pattern|cruise climb technique]] is trying to solve.

So using the [[lift equation]] we know: $L=\frac{1}{2}\rho V^{2}SC_L$

To keep lift equal to weight as the fuel is burned we therefore must change one of the following:
- $\rho$
- $V$
- $C_L$

The technique we are focusing on here is going to assume that true airspeed and angle of attack are constant [[Effect of angle on lift coefficient|(because lift coefficient's a function of angle of attack)]].

#### Calculating changes required
If $C_L$ is constant then:
$$\begin{align*}
   \frac{L}{D} &= \frac{C_L}{D_D}\\
&= \dfrac{C_L}{C_{D0} + \dfrac{KC_L^{2}}{\pi A} } 
\end{align*}$$
hence $\frac{C_L}{C_{D0} + \frac{KC_L^{2}}{\pi A} }$ will also be constant. ([[Drag coefficient|where we got the equation from]])

Now if we recall the [[Breguet range equation]]: $R = \frac{1}{s} \frac{VL}{D} \ln\left(1+\frac{W_f}{W_s}\right)$