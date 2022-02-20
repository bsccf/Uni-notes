---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe the
## Generalised hookes law
Basically eveything on [[plane stress (generalised hookes law)|plane stress]] is just [[generalised hookes law]] with no stress in zz, so this is the more painful version.

Consider this cube:

![[Pasted image 20220220113951.png]]

Now for the cube you can use the following equations for things and stuff:

### Strains
#### Axial
> ### $$ \varepsilon_{xx} = \frac{\sigma_{xx} - \nu(\sigma_{yy} + \sigma_{zz})}{E} $$ 
> ### $$ \varepsilon_{yy} = \frac{\sigma_{yy} - \nu(\sigma_{xx} + \sigma_{zz})}{E} $$ 
> ### $$ \varepsilon_{zz} = \frac{\sigma_{zz} - \nu(\sigma_{yy} + \sigma_{xx})}{E} $$ 
>> where:
>> $\varepsilon=$ strain in some ax
>> $\sigma=$ stress
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]

#### Shear
The equations for $\varepsilon_{xy},\varepsilon_{xz},\varepsilon_{yz}$ are all the same, just replace the $\sigma$ and $\varepsilon$ in the equation below: 
> ### $$ \begin{align*} \varepsilon_{xy} &= \frac{1+\nu}{E} \sigma_{xy} &\varepsilon_{xz} &= \frac{1+\nu}{E} \sigma_{xz} &\varepsilon_{yz} &= \frac{1+\nu}{E} \sigma_{yz}\end{align*} $$ 
>> where:
>> $\varepsilon_{xy}=$ shear strain in xy
>> $\sigma_{xy}=$ shear stress in xy
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]

