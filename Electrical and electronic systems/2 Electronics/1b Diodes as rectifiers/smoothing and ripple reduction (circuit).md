---
aliases: ["wave smoothing and ripple reduction"]
tags: ["Question","QFormat3"]
---

#### What is
## Smoothing and ripple reduction (circuit)
### Introduction
So if we look at [[full-wave rectification]] and [[half-wave rectification]] we can see that even though the voltage sign is constant the magnitude is constantly changing, even the glorious [[full-wave rectification|FULL BRIDGE RECTIFIER!!!!]] suffers from this problem, and yes I am leaving exclamation points mid sentence.
So we use [[smoothing and ripple reduction (circuit)|wave smoothing and ripple reduction]] by using components that have useful time dependent properties.

### Using [[Capacitors|capacitors]]
It is possible to make a [[full-wave rectification|FULL BRIDGE RECTIFIER!!!!]] even more perfect by adding a smoothing [[Capacitors|capacitor]] as shown:
![[Pasted image 20211217162252.png]]
Since the capacitor charges and discharges depending on the cycle position it leads to a pd/time graph like:
![[Pasted image 20211217162455.png]]
As the [[capacitance]] of the capacitor increases the $\Delta V$ decreases, consequently if the $\Delta t$ increases the $\Delta V$ increases. So we can reduce peaks with stronger [[Capacitors|capacitors]] or by increasing the frequency of the AC.
In reality you don't need a perfect constant supply voltage, your use case will have an acceptable range of voltages, currents and rate of change of these, so basically we just need the ripple reduction to be "good enough".

#### Deriving equations
If we want nice equations to calculate the expected smoothing we can derive them.
Starting with the capacitor equation:

$$\begin{align*}
Q &= CV\\
\frac{dQ}{dt} &= C \frac{dV}{dt}\\
i_{DC} &= C \frac{dV}{dt}
\end{align*}$$

If you look back at our ripple graph, the shape can be approximated as triangular so to make working ez we are going to do just that:

$$\begin{align*}
i_{DC} &= C \frac{\Delta V}{ \Delta t }
\end{align*}$$

