---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Taylor series
### Method
In mathematics, the Taylor series of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point.

For a given function ($f(x)$) it's [[Taylor series]] can be defined at a value of x (where $x=a$), by the following equation:

> ### $$ \sum\limits_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n} $$
> ### $$or$$
> ### $$ f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4} + ... $$ 
>> where:
>> $f^{(n)}(a)=$ nth derivative of $f(a)$

It is an increasingly accurate approximation of the function $f(a)$.

There is a special case of the [[Taylor series]], which is when $a=0$ we call this a [[Maclaurin series]].

### Examples

> Use [[Taylor series]] to find an approximate value of:
> $$ f(x) = \frac{1}{x-3} $$
> at $x=4$

$$\begin{align*}
 f(x) &= \frac{1}{x-3} = (x-3)^{-1} & f(4)&=(4-3)^{-1}=&1\\
f^{'}(x) &= -(x-3)^{-2} & f^{'}(4)&=-(4-3)^{-2}=&-1\\
f^{''}(x) &= 2(x-3)^{-3} & f^{''}(4)&=2(4-3)^{-3}=&2\\
f^{'''}(x) &= -6(x-3)^{-4} & f^{'''}(4)&=-6(4-3)^{-4}=&-6\\
f^{''''}(x) &= 24(x-3)^{-5} & f^{''''}(4)&=24(4-3)^{-5}=&24
\end{align*}$$

$$\begin{align*}
\frac{1}{4-3} &\approx f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4}\\
&\approx 1 + \frac{ -1 }{1}(x-4) + \frac{ 2 }{2}(x-4)^{2}+ \frac{ -6 }{6}(x-4)^{3}+ \frac{ 24 }{24}(x-4)^{4}\\
&\approx 1 -(x-4) + (x-4)^{2}-(x-4)^{3}+ (x-4)^{4}
\end{align*}$$
