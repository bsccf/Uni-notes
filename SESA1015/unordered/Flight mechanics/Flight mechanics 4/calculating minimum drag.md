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

Then using [[Lift equation#^{1f2714]] rearranged to: $\dfrac{2L}{\rho V^{2}S} =  C_L$

$$ \begin{align*}
D =& \frac{1}{2}\rho V^{2}S (C_{Do} + \dfrac{K}{\pi A} \cdot (\dfrac{2L}{\rho V^{2}S})^{2})\\
=&  \frac{1}{2}\rho V^{2}S C_{Do} + \frac{1}{2}\rho V^{2}S \dfrac{K}{\pi A} \cdot \dfrac{4L^{2}}{\rho^{2} V^{4}S^{2}}\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{\rho V^{2} S K 4L^{2}}{2 \pi A \rho^{2} V^{4}S^{2}} & W&=L\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{2 K W^{2}}{ \rho \pi A V^{2}S }\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{2 K}{ \pi A} \cdot \frac{ W^{2}}{ \rho S V^{2} }
\end{align*} $$

#### Final equation

Hence focusing on speed:

> $$ D = A'V^{2} + \frac{B'}{V^{2}} $$ 
>> where:
>> $D=$ Drag 
>> $V=$ [[True airspeed]]
>> $A'=$ A constant
>> $B'=$ A constant
>> (They are only constants in steady flight)

### Implications
![[Pasted image 20211101214128.png]]
This equation $D = A'V^{2} + \frac{B'}{V^{2}}$ implies that for any