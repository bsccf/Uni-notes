---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What?
## The Macaulary method
The Macaulary method.

### Why we need it

Ok so if we look back at our [[Deflection in beams notes]] and the example that had multiple sections that you had to calculate:
[[examples of calculating deflection of a beam#Example 2]]

You can see things become a massive pain in the ass when this sort of stuff get's introduced, so this [[chad called Macaulary]] realized that we can simplify things with... a method, not sure you know the name, but it is:

### The Macaulary method

> ### $$ \left( x-k \:\:\: \{x-k\geq 0\}\right) = [x-k] $$ 
>> where:
>> $x=$ A variable
>> $k=$ A constant

Basically it the bit in the brackets can't be less than zero, if $x<k$ then it is equal to zero. It's simple but we can use this in beams to describe moments, shear force and deflection along a beam with much less equations.

#### Differentiation and intergration
> ### $$ \frac{d}{dx}a[x-k]^b = ab[x-k]^{b-1} $$
> ### $$ \int a[x-k]^{b} \cdot dx = \frac{a[x-k]^{b+1}}{b+1} $$

### Taking the same [[examples of calculating deflection of a beam#Example 2|example]]

![[Pasted image 20211122180700.png]]

#### Plotting its resault
![[Pasted image 20211122180402.png]]
![[Pasted image 20211122180429.png]]
![[Pasted image 20211122180458.png]]

#### Implications
This graph suggests that the highest deflection will occur when the load is applied at the centre of the beam