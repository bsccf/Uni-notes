---
aliases: ["plane stress","plane strain","plane stress equations","plane stain equations"]
tags: ["Question","QFormat3"]
---

#### Describe
## Plane stress (generalised hookes law)
So in the past we discussed [[poisson's ratio]] and we have been mostly solving problems with loads in one diection, but when working in 3D or even 2D there are often stresses and strains being externally applied in multiple directions, so the [[poisson's ratio]] needs to be used to calculate how all these different stresses interact and overlap. So it is important to keep in mind that these equations need to be used instead of there simpler older counterparts when considering multi directional strain situations!

![[Pasted image 20220220111356.png]]

In a situation of plane stress we assume $\sigma_{zz}=0$ but that does not mean that $\varepsilon_{zz}=0$, using this we can derive the following formula for strains:

### Strain equations

#### X Strain

> ### $$ \varepsilon_{xx} = \frac{1}{E} (\sigma_{xx} - \nu \sigma_{yy} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{xx}=$ strain in xx
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\sigma_{zz}=0=$ stress in zz
>> $\nu=$ [[poisson's ratio]]

#### Y Strain

> ### $$ \varepsilon_{yy} = \frac{1}{E} (\sigma_{yy} - \nu \sigma_{xx} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{yy}=$ strain in yy
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\sigma_{zz}=0=$ stress in zz
>> $\nu=$ [[poisson's ratio]]

#### Z Strain

> ### $$ \varepsilon_{zz} = -\frac{\nu}{E} (\sigma_{xx} + \sigma_{yy} ) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{zz}=$ strain in zz
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\nu=$ [[poisson's ratio]]

#### [[local shear strain|shear strain]]

![[Pasted image 20220220112430.png]]

> ### $$ \varepsilon_{xy} = \frac{1+\nu}{E} (\sigma_{xy}) $$ 
>> where:
>> $E=$ [[youngs modulus]]
>> $\varepsilon_{xy}=$ shear strain in xy
>> $\sigma_{xx}=$ shear stress in xy
>> $\nu=$ [[poisson's ratio]]

### Stress equations
With lots of subbing in and rearranging you can get the following stress equations from the strain ones:

#### X stress

> ### $$ \sigma_{xx} = \frac{E}{1-\nu^{2}} ( \varepsilon_{xx} + \nu \varepsilon_{yy} ) $$ 
>> where:
>> $\sigma_{xx}=$ stress in x
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]
>> $\varepsilon_{xx}=$ strain in x
>> $\varepsilon_{yy}=$ strain in y

#### Y stress

> ### $$ \sigma_{yy} = \frac{E}{1-\nu^{2}} ( \varepsilon_{yy} + \nu \varepsilon_{xx} ) $$ 
>> where:
>> $\sigma_{yy}=$ stress in y
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]
>> $\varepsilon_{xx}=$ strain in x
>> $\varepsilon_{yy}=$ strain in y

#### Z Stress

> ### $$ \sigma_{zz} = 0 $$
>> Because:
>> That is [[I am concerned if you didn't realise that|literally the point]] of this page, have you not been paying attention?

#### Shear stress

> ### $$ \sigma_{xy} = \frac{E}{1+\nu} \varepsilon_{xy} $$ 
>> where:
>> $\sigma_{xy}=$ shear stress in xy
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]
>> $\varepsilon_{xy}=$ shear strain in xy