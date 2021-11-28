---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Taylor series
### Method
In mathematics, the Taylor series of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point.

A Taylor Series simply approximates a function around a point. Basically, you take a point, and use the derivative to figure out how much the function would change if you move away from that point. And then use the second derivative to refine your guess on how much it would move. And the third, and so on until you get accurate enough. A Taylor Series is basically math-speak for just eyeballing it.

For a given function ( $f(x)$ ) it's [[Taylor series]] can be defined as:

> ### $$ \sum\limits_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n} $$
> ### $$or$$
> ### $$ f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4} + ... $$ 
>> where:
>> $f^{(n)}(a)=$ nth derivative of $f(a)$
>> $a=$ a point near x



It is an increasingly accurate approximation of the function $f(a)$.

If we let $x=a$:
$$\begin{align*}
   f(x) &= f(x) + \frac{f^{'}(x) }{1!}(x-x) + \frac{f^{''}(x) }{2!}(x-x)^{2}+ \frac{f^{'''}(a) }{3!}(x-x)^{3}+ \frac{f^{''''}(a) }{4!}(x-x)^{4} + ...\\
&= f(x)
\end{align*}$$
You can see that the two formula are perfectly equal, so now consider a value of $a=x+0.01$ then the $(x-a)^{n}$ becomes $(x-(x+0.01))^{n}(-0.01)^{n}$ which rapidly tends towords 0. Hence for values of a which are in the range $-1<a<1$ we know $(x-a)^{n}$ will tend to 0:
$$\begin{align*}
   f(x+a) &= f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4} + ... & &let\:a=x+m\\
&= f(x+m) + \frac{f^{'}(x+m) }{1!}(x-(x+m)) + \frac{f^{''}(x+m) }{2!}(x-(x+m))^{2}+ \frac{f^{'''}(x+m) }{3!}(x-(x+m))^{3}+ \frac{f^{''''}(x+m) }{4!}(x-(x+m))^{4} + ...\\
&= f(x+m) + \frac{f^{'}(x+m) }{1!}(m) + \frac{f^{''}(x+m) }{2!}(m)^{2}+ \frac{f^{'''}(x+m) }{3!}(m)^{3}+ \frac{f^{''''}(x+m) }{4!}(x-(x+m))^{4} + ...
\end{align*}$$

There is a special case of the [[Taylor series]], which is when $a=0$ we call this a [[Maclaurin series]]. This is like 99% of the use of the [[Taylor series]].