---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Operator notation
### Stuff
Since functions can be passed as parameters it is also possible to define a function interms of the function passed to it:

> ### $$ \phi[ f(x) ] $$ 
>> where:
>> $\phi[...]=$ A function that takes a function as input 
>> $f(x)=$ A function

I don't think square brackets are manditory, but they seem like a good way to show that the function takes other functions as inputs.

### Examples
#### Example 1
$$\begin{align*}
 \phi[ f(x) ] &= \frac{(f(x))^{2}}{5} + \frac{d}{dx} f(x) - \frac{f(x)}{f(x)-1}
\end{align*}$$

#### Example 2
$$\begin{align*}
 \phi[ f(x) ] &= f(x+5) + \frac{d}{dx} f(x)
\end{align*}$$

#### Example 3

I think you should be able to define these recursively, though in most cases that would probably resault in some infinately increasing value:

$$\begin{align*}
\phi[ f(x) ] &= \phi[ \phi[ f(x) ]  ] 
\end{align*}$$
