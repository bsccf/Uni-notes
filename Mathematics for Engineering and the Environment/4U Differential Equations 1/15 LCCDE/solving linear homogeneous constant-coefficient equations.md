---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Solving linear homogeneous constant-coefficient equations
![[linear homogeneous constant-coefficient equation#^9a6d21]]

1) 
> Treat it like a quadratic and find it's roots:
> $$ \begin{align*}
a \frac{d^{2}x}{dt^{2}}+ b \frac{dx}{dt} + cx &= 0 &\to&& am^{2}+bm+c&=0\\
&& roots:\:&m_1,m_2
\end{align*} $$
2) 
> Depending on what roots are found one of the following formats is used:
>> ### $$ x(t) = Ae^{m_1 t} + Be^{m_2 t} $$ 
>>> when:
>>> $m_1,m_2=$ real numbers
>>> $m_1=m_2$
>>
>>> where:
>>> $A,B$ = constants
>
>> ### $$ x(t) = (At+B)e^{m_1 t} $$ 
>>> when:
>>> $m_1,m_2=$ real numbers
>>> $m_1 \neq m_2$
>>
>>> where:
>>> $A,B$ = constants 
>
>> ### $$ x(t) = e^{at} ( A\cos(bt) + B\sin(bt) ) $$ 
>>> when:
>>> $m_1,m_2=$ complex numbers
>>
>>> where:
>>> $A,B$ = constants
>>> $root=a\pm bi$
>
