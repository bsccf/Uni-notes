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
#### Strain in x
> ### $$ \varepsilon_{xx} = \frac{\sigma_{xx} - \nu(\sigma_{yy} + \sigma_{zz})}{E} $$ 
>> where:
>> $\varepsilon_{xx}=$ strain in xx
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{zz}=$ stress in yy
>> $\sigma_{yy}=$ stress in zz
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]

#### Strain in y
> ### $$ \varepsilon_{yy} = \frac{\sigma_{yy} - \nu(\sigma_{xx} + \sigma_{zz})}{E} $$ 
>> where:
>> $\varepsilon_{yy}=$ strain in yy
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{zz}=$ stress in yy
>> $\sigma_{yy}=$ stress in zz
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]

#### Strain in z
> ### $$ \varepsilon_{zz} = \frac{\sigma_{zz} - \nu(\sigma_{yy} + \sigma_{xx})}{E} $$ 
>> where:
>> $\varepsilon_{zz}=$ strain in zz
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{zz}=$ stress in yy
>> $\sigma_{yy}=$ stress in zz
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]

#### Strain in xy,x
The equations for
> ### $$ \varepsilon_{xy} = \frac{1+\nu}{E} \sigma_{xy} $$ 
>> where:
>> $\varepsilon_{xy}=$ shear strain in xy
>> $\sigma_{xy}=$ shear stress in xy
>> $E=$ [[youngs modulus]]
>> $\nu=$ [[poisson's ratio]]