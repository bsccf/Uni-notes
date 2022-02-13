---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Local shear strain
### Useful bit
![[Pasted image 20220213104635.png]]

> ### $$ \gamma_{xy} = \alpha + \beta = \frac{du_{x}}{dy} + \frac{du_{y}}{dx} $$ 
>> where:
>> $=$ 
>> $=$
>> $=$

### Explenation
Basically the same as [[local strain]] but considering [[shear strain]] instead:
![[Pasted image 20220213104133.png]]

We can generate the following equation for finding the gradient for the case above:
$$ \frac{du_{x}}{dy} = \frac{u_{x\:top}-u_{x\:bottom}}{dy} $$

Now if we consider what this looks like for a small material element with initial dimensions $dx$ and $dy$, where the object is free to rotate:

![[Pasted image 20220213104635.png]]

Which if we take small angle approximations becomes:

$$ \gamma_{xy} = \alpha + \beta = \frac{du_{x}}{dy} + \frac{du_{y}}{dx} $$

It should be noted that shear strain is essentially a measure of the change in angle between the x and y sides from 90 degrees, so sign matters:

![[Pasted image 20220213105020.png]]

While:
![[Pasted image 20220213105130.png]]