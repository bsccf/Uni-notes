---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What
## Calculating limits on preformance for a co-ordinated turn

Our course is pointless, the internet found a better method of flight [[watching this]].

### Introduction

We have this useful boi that we calculated previously:
![[calculating lift in a co-ordinated turn#^6e5848]]

We know each of these values have limitations, things like max lift coefficient, [[stalling speed]], even [[yield strength|yield stress]] and limitations on the forces the aircraft can experience. So lets rearrange our lift equation to analyse how these limitations effect our flight.

### Radius rearrangement
#### Math

$$\begin{align*}
 L &= W \sqrt{ 1 + \left(\frac{V^{2}}{gR}\right)^{2} }\\
\frac{L^{2}}{W^{2}} - 1 &= \left(\frac{V^{2}}{gR}\right)^{2}\\
\frac{g}{V^{2}} \sqrt{\frac{L^{2}}{W^{2}} - 1} &= \frac{1}{R}\\
\therefore R &= \frac{V^{2}}{g\sqrt{\frac{L^{2}}{W^{2}} - 1}}
\end{align*}$$

You can also express this interms of bank angle and speed, (the equations used here are from [[modeling a co-ordinated turn]]):

$$\begin{align*}
  L sin\phi  &= \frac{W}{g} \frac{V^{2}}{R}\\
 R   &= \frac{WV^{2}}{Lg \cdot sin\phi} & L\cos\phi = W \\\\
&= \frac{L\cos\phi\cdot V^{2}}{Lg \cdot sin\phi}\\
&= \frac{ V^{2}}{g \cdot tan\phi}
\end{align*}$$

As we can see, by increasing the [[bank angle]] we can decrease the radius of turning.

![[minimum radius of turning during a co-ordinated turn#Minimum radius of turning during a co-ordinated turn]]

### The limit part
![[limit on the load factor during a co-ordinated turn#Limit on the load factor during a co-ordinated turn]]

![[limit on the ]]