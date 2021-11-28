---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Maclaurin series
### Meth
This is a special form of the [[Taylor series]] where $a=0$






### Equation
> Use the [[Maclaurin series]] to find an approximate value of:
> $$ f(x) = \frac{1}{x-3} $$
> where $x=4$

$$\begin{align*}
 f(x) &= \frac{1}{x-3} = (x-3)^{-1} & f(0)&=(4-3)^{-1}=&1\\
f^{'}(x) &= -(x-3)^{-2} & f^{'}(0)&=-(4-3)^{-2}=&-1\\
f^{''}(x) &= 2(x-3)^{-3} & f^{''}(0)&=2(4-3)^{-3}=&2\\
f^{'''}(x) &= -6(x-3)^{-4} & f^{'''}(0)&=-6(4-3)^{-4}=&-6\\
f^{''''}(x) &= 24(x-3)^{-5} & f^{''''}(0)&=24(4-3)^{-5}=&24
\end{align*}$$

Now we can sub into the equation:

$$\begin{align*}
\sum\limits_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n} &\approx f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4}\\\\
&
\end{align*}$$

