---
aliases: ["integration to find the center of a laminar"]
tags: ["Question","QFormat3"]
---

#### How can we find the
## Centroid of a plane area
### General case
Given that a 2D shape is defined as the area between two curves between two limits:
![[Pasted image 20211223105935.png]]
It's possible to find the center of this shape using:
> ### $$ \bar{y} = \frac{1}{2A} \int^{b}_a \left( [f(x)]^{2} - [g(x)]^{2} \right)  \cdot dx $$ 
>> where:
>> $A= \int^{b}_a [f(x)-g(x)]\cdot dx$ 
>> $\bar{y} =$ center of y
>> $a,b=$ limits
>> $f(x),g(x)=$  functions that define the curve
>> $f(x) \geq g(x)$

> ### $$ \bar{x} = \frac{1}{A} \int^{b}_a x[ f(x) - g(x) ] \cdot dx $$
>> where:
>> $A= \int^{b}_a [f(x)-g(x)]\cdot dx$ 
>> $\bar{x} =$ center of x
>> $a,b=$ limits
>> $f(x),g(x)=$  functions that define the curve
>> $f(x) \geq g(x)$

### Along the x axis
If we let $y=0$ 