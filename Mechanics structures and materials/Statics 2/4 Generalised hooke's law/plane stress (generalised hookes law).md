---
aliases: ["plane stress","plane strain","plane stress equations","plane stain equations"]
tags: ["Question","QFormat3"]
---

#### Describe
## Plane stress (generalised hookes law)
So in the past we discussed [[poisson's ratio]] and we have been mostly solving problems with loads in one diection, but when working in 3D or even 2D there are often stresses and strains being externally applied in multiple directions, so the [[poisson's ratio]] needs to be used to calculate how all these different stresses interact and overlap.

![[Pasted image 20220220111356.png]]

In a situation of plane stress we assume $\sigma_{zz}=0$ but that does not mean that $\varepsilon_{zz}=0$, using this we can derive the following formula for strains:

> ### $$ \varepsilon_{xx} = \frac{1}{E} (\sigma_{xx} - \nu \sigma_{yy} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{xx}=$ strain in xx
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\nu=$ [[poisson's ratio]]

> ### $$ \varepsilon_{yy} = \frac{1}{E} (\sigma_{yy} - \nu \sigma_{xx} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{yy}=$ strain in yy
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\nu=$ [[poisson's ratio]]

> ### $$ \varepsilon_{zz} = -\frac{\nu}{E} (\sigma_{xx} + \sigma_{yy} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{zz}=$ strain in zz
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\nu=$ [[poisson's ratio]]

