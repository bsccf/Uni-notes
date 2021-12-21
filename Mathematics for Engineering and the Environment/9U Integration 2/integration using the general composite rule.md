---
aliases: ["integration substitution method","integration by substitution"]
tags: ["Question","QFormat3"]
---

#### What is
## Integration using the general composite rule

> ### $$ \int f^{'}(g(x))\times g^{'}(x)\cdot dx = f(g(x))+k $$ 
>> where:
>> $f(x),g(x)=$ a function 
>> $k=$ a constant

The hard part of using this is getting/seeing that the equation is in that format.

Alternatively you can replace g(x) with t (or some other letter) and use:

> ### $$ \int f^{'}(g(x))\times g^{'}(x)\cdot dx = \int f^{'}(t) \frac{dt}{dx} dx = \int f^{'}(t) dt = f(t) + k $$ 
>> where:
>> $f(t)=$ a function 
>> $k=$ a constant

(This second one is the way you really use it tbh)

### Examples
#### Example 1
> Find the [[Indefinate integral]] of $\int 2x\sqrt{x^{2}+2}\cdot dx$

$$\begin{align*}
&\int 2x\sqrt{x^{2}+2}\cdot dx \\
&&& t = x^{2}+2\\
&&& \frac{dt}{dx} = 2x\\
&\int \frac{dt}{dx} \sqrt{t}\cdot dx\\
&\int \sqrt{t} \cdot dt\\
& \frac{2}{3} t^{\frac{3}{2}} + k\\
& \frac{2}{3} (x^{2}+2)^{\frac{3}{2}} + k
\end{align*}$$

#### Example 2

>
