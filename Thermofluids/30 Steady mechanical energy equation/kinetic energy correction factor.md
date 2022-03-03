---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Kinetic energy correction factor ($\alpha$)
Basically this thing is used to account for the uneven distrobution of mass flow through a cross section due to friction with the wall:
![[Pasted image 20220303164904.png]]
On the left is an ideal situation while the right is more realistic, so we don't have to deal with the headache of calculating it ourselves you usually get given it but heres the formula:

> ### $$ \alpha =  \frac{ KE_{actual\:velocity}}{KE_{average\:velocity}} = \frac{\frac{1}{2} dm U^{2} }{\frac{1}{2} dm \bar{U}^{2} }= \frac{ U^{2} }{ \bar{U}^{2} } $$ 
> ### $$ \alpha \times KE_{average\:velocity} =  KE_{actual\:velocity}  $$ 
>> where:
>> $=$ 
>> $=$
>> $=$

### Example
Find the [[kinetic energy correction factor]] for a pipe where the velocity of the fluid can be described using the function $f(r)=\left(\frac{R-r}{R}\right)^{2}$:
![[Pasted image 20220303170443.png]]
[[volume of a solid of revolution|volume of revolution]]

$$\begin{align*}
f &= \left(\frac{R-r}{R}\right)^{2} &f(r)_{max} &= \left(\frac{R-0}{R}\right)^{2}\\
R-R\sqrt{f} &= r &&= 1\\
R(1-\sqrt{f}) &= r
\end{align*}$$

$$\begin{align*}
T \bar{U} R^{2} &= k T \pi \int^{1}_{0} (r)^{2} \cdot dr\\
T \bar{U} R^{2} &= k T \pi \int^{1}_{0} (R(1-\sqrt{f}))^{2} \cdot dr\\
T \bar{U} R^{2} &= k T \pi R^{2} \int^{1}_{0} r+1-2\sqrt{f} \cdot dr\\
T \bar{U} R^{2} &= k T \pi R^{2} [ r+1-2\sqrt{f} ]^{1}_{0}\\
\end{align*}$$