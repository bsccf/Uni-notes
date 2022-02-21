---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Stress transformation for uniaxle loading
### Equations
![[Pasted image 20220221125353.png]]

> ### $$ \sigma_{x'x'} =\sigma_{xx} \cos^{2}\theta $$ 
>> where:
>> $\sigma_{x'x'}=$ normal stress on slice
>> $\sigma_{xx}=$ stress parrallel to external uniaxle loading
>> $\theta=$ angle of slice

> ### $$ \sigma_{x'y'} = \sigma_{xx}\sin\theta \cos\theta $$ 
>> where:
>> $\sigma_{x'y'}=$ shear stress along slice
>> $\sigma_{xx}=$ stress parrallel to external uniaxle loading
>> $\theta=$ angle of slice

### Proof
The important thing to understand about stresses is their values depend on the direction used as axis, for uniaxle loading we only have external forces acting in one direction but we can find the stress at different inclined slices through the object which are also valid interpretations of stress just relative to a different axis.

Heres a diagram represening uniaxial loading and a slice at angle theta through it:

![[Pasted image 20220221124420.png]]

It should now be noted that the total force through this slice will be equal to the force through a non angled slice:

![[Pasted image 20220221124604.png]]

So if we define the normal and perpendicular force as components of the force unrotated force we get the following:
$$\begin{align*}
F_{N} &= F \cos\theta & F_{S}&= F\sin\theta 
\end{align*}$$

Now we can also define the area of this slice as:
$$\begin{align*}
A_{\theta} &= \frac{A}{\cos\theta}
\end{align*}$$


![[Pasted image 20220221125036.png]]

So finally it becomes possible to define shear and normal stresses by dividing force by area:

$$\begin{align*}
\sigma_{x'x'} &= \frac{F \cos\theta}{\frac{A}{\cos\theta}} & \sigma_{x'y'} &= \frac{F\sin\theta }{\frac{A}{\cos\theta}}\\
&=\frac{ F}{A} \cos^{2}\theta & &=\frac{F}{A} \sin\theta \cos\theta\\
&=\sigma_{xx} \cos^{2}\theta  & &= \sigma_{xx}\sin\theta \cos\theta 
\end{align*}$$