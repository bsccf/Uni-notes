---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating minimum drag
### Conditions
We can work under the same assumtions from [[steady flight and true airspeed#Conditions]].

### Calcualations
We know that drag can be found using:
![[Drag equation#^33fc8d]]

Subbing in for $C_D$ with:
[[Drag coefficient#^e6ae2f]]

Then subbing in $C_{Di}$ with:
[[induced drag coefficient#^4d0b00]]
[[induced drag coefficient#^438b96]]

$C_{Di} = \dfrac{K}{\pi A} C_L^{2}$

We get:
$$\begin{align*}
D =& \frac{1}{2}\rho V^{2}S (C_{Do} + C_{Di})\\
=& \frac{1}{2}\rho V^{2}S (C_{Do} + \dfrac{K}{\pi A} C_L^{2})
\end{align*} $$

Then using [[Lift coefficient]]