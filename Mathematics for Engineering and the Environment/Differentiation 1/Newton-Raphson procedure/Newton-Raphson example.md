---
aliases: [""]
tags: ["Question","QFormat1"]
---

## Newton-Raphson example
### Problem
Find a root of $8x^4+0.45x^3-4.544x-0.1136=0$ to 4d.p near $x=0.8$

### Method
Using [[Newton-Raphson]]

> taking $f(x) = 8x^4+0.45x^3-4.544x-0.1136$
> $$ \begin{align*}
f(x) &= 8x^4+0.45x^3-4.544x-0.1136\\
\dot{f}(x) &= 32x^3+1.35x^2-4.544\\
x_{n+1} &= x_{n} - \dfrac{f(x_n)}{\dot{f}(x_n)}\\
x_{n+1} &= x_{n} - \dfrac{8x^4+0.45x^3-4.544x-0.1136}{32x^3+1.35x^2-4.544}
\end{align*}$$