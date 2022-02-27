---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe how you solve
## Doube integrals with dependent limits
So you know how I said that [[double integrals with independent limits|double integrals]] are easy, they only become difficult when limits get fucky well that's what this is about. What it essentially comes down to is the fact that to integrate something you have to fully expand all variables that can be defined interms of the variable your integrating for. For example if you have a function $y(x)$ where $y = x+2$ if you have to integrate $\int xy dx$ then:
$$\begin{align*}
\int xy \cdot dx &\\
\int x(x+2) \cdot dx &\\
\int x^{2}+2x \cdot dx &\\
\frac{x^{3}}{3} + x^{2} & 
\end{align*}$$
It would be wrong to do:
$$\begin{align*}
\int xy \cdot dx &\\
y\int x \cdot dx &\\
y \frac{x^{2}}{2} &\\
\end{align*}$$
This is what I mean by fully expanding all variables that can be defined interms of what's being integrated for, since y can be defined interms of x it must be accounted for. So in this exact same way given the following example:
> Solve:
> $$ V = \int^{X}_{0} \int^{g}_{0} yx+1 \cdot dy \cdot dx $$
> where: $g = x^{2}$

Here although y is an independent variable from x you can rewrite the integral as:

$$ \int^{X}_{0} f(x) \cdot dx $$

where: $f(x) = \int^{g}_{0} yx+1 \cdot dy$, so by thinking about it that way you can clearly see that integration order matters in these situations. Now if for some reason you wanted to integrate for x first you would need to change the limits so that your dy integral is no longer a function of x.