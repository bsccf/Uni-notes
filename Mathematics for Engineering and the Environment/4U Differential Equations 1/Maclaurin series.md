---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Maclaurin series
### Meth
This is a special form of the [[Taylor series]] where $a=0$, here are what that resaults in:

$$\begin{align*}
f(x+a) &= f(a) + \frac{f^{'}(a) }{1!}x + \frac{f^{''}(a) }{2!}x^{2}+ \frac{f^{'''}(a) }{3!}x^{3}+ \frac{f^{''''}(a) }{4!}x^{4} + ...\\
& & &let\:a=0\\\\
f(x+0) &= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ...\\
f(x) &= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ...
\end{align*}$$

Hence any function can be calculated by:

> ### $$ f(x)= f(0) + \frac{f^{'}(0) }{1!}x + \frac{f^{''}(0) }{2!}x^{2}+ \frac{f^{'''}(0) }{3!}x^{3}+ \frac{f^{''''}(0) }{4!}x^{4} + ... $$ 
>> where:
>> 

$$\begin{align*}
 f(x) &= \frac{1}{x-3} = (x-3)^{-1} \\
f^{'}(x) &= -(x-3)^{-2} \\
f^{''}(x) &= 2(x-3)^{-3} \\
f^{'''}(x) &= -6(x-3)^{-4} \\
f^{''''}(x) &= 24(x-3)^{-5} 
\end{align*}$$

Now we can sub into the equation:

$$\begin{align*}
\sum\limits_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^{n} &\approx f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4} & let\: a&=0\\
&\approx f(a) + \frac{f^{'}(a) }{1!}(x-a) + \frac{f^{''}(a) }{2!}(x-a)^{2}+ \frac{f^{'''}(a) }{3!}(x-a)^{3}+ \frac{f^{''''}(a) }{4!}(x-a)^{4}
\end{align*}$$

