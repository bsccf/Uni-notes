---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Stress transformation for plane stress


### Proof
Basically the same as [[stress transformation for uniaxle loading#Proof]] but now in 2D. (so [[something something skill issue|harder]])

Since we have multiple forces acting in each axis we need to account for all their components effect on forces acting on rotated planes:
![[Pasted image 20220221134050.png]]

But we can change our diagram to represent an equivalent pressure in a way that's less overwhelming:
![[Pasted image 20220221134202.png]]

As before we can use pressure times area to get force and then equilibrium conditions to get equations defining the stress on/along the plane we are intrested in:
$$\begin{align*}
A_{y} &= A & A_{x} &= A\tan\theta & A_{H} &= \frac{A}{\cos\theta} 
\end{align*}$$
For cancelling terms later it will be convenient to define the area of the faces interms of a single area $A$, now to get our force equilibrium equations along the normal/tangent of the cut face and solve:
$$\begin{align*}
\sigma_{x'x'} A_{H} &=  
\end{align*}$$