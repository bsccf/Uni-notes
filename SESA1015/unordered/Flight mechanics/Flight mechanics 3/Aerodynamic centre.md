---
aliases: [""]
tags: ["Question","QFormat3","SESA1015"]
---

#### What is the
## Aerodynamic centre
This is defined as the reference axis position about which the pitching moment coefficient does not  vary with angle of attack. In maths terms:
$$ \frac{dM_{AC}}{d\alpha}=0 $$
In other terms:
The Aerodynamic center is the point at which the pitching moment coefficient for the airfoil does not vary with lift coefficient (i.e. angle of attack), making analysis simpler.

The lift and drag forces can be applied at a single point (the [[Centre of pressure]]), about which they exert zero torque, but this is impractical for analysis as the [[Centre of pressure]]'s location varies greatly with angle of attack. So this is why the aerodynamic centre is used.

![[Pasted image 20211021205317.png]]

Taking moments about the centre of gravity:
$$ M_{CG} = M_0 + x_{AC}L $$

Then if we divide by $\frac{1}{2}\rho V^{2}Sc$ and use $C_m = C_{mo}-hC_L$ (from [[Effect of angle of attack on the moment coefficient#^cfc8b1]]):

> $$ C_{CG} = C_{M_0} \dfrac{x_{AC}}{c}C_L = C_m - hC_L $$ 
>> where:
>> $C_{CG} =$  moment coefficient around the centre of gravity
>> $x_{CP} =$ distance between centre of pressure and centre of gravity
>> $c =$ [[Mean chord|Mean aerodynamic chord]]
>> $C_L =$ [[Lift coefficient]]
>> $h =$ a constant

