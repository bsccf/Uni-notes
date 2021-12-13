---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Operator notation
### Stuff
Since functions can be passed as parameters it is also possible to define a function interms of the function passed to it:

> ### $$ \phi[ f(x) ] \:\:\: or \:\:\: \phi f(x) $$ 
>> where:
>> $\phi[...]=$ A function that takes a function as input 
>> $f(x)=$ A function

I don't think square brackets are manditory, but they seem like a good way to show that the function takes other functions as inputs.

### Examples
#### Example 1
$$\begin{align*}
 \phi[ f(x) ] &= \frac{(f)^{2}}{5} + \frac{d}{dx} f - \frac{f}{f-1}
\end{align*}$$

#### Example 2
$$\begin{align*}
 \phi[ f(x) ] &= f(x+5) + \frac{d}{dx} f(x)
\end{align*}$$

As you can see you can use $f$ or $f(x)$ on the right. I thing $f(x)$ provides more clarity tbh

#### Example 3

I think you should be able to define these recursively, though in most cases that would probably resault in some infinately increasing value:

$$\begin{align*}
\phi[ f(x) ] &= v( \phi[ f(x) ] )\\
&=  v(v(v(v(v(v(v(v(v(v(v(v(... f(x) ...))))))))))))\\
&= v^{\inf}f(x)
\end{align*}$$

Some cases it would tend to a value, not sure if this is valid syntax.