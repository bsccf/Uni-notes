---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are some
## Common substitutions for integration
### Common situations
| if $f(x)$ contains      | try (for x)      | try for $dx/d$                                 |
| ----------------------- | ---------------- | ---------------------------------------------- |
| $\sqrt{a^{2} - x^{2}}$  | $x=a\sin\theta$  | $\frac{dx}{d\theta}= a\cos\theta$              |
| $\sqrt{a^{2} - x^{2}}$  | $x=a\tanh u$     | $\frac{dx}{du}=a sech^{2} u$                   |
| $\sqrt{a^{2} + x^{2}}$  | $x=a \sinh u$    | $\frac{dx}{du} = a\cosh u$                     |
| $\sqrt{a^{2} + x^{2}}$  | $x=a\tan \theta$ | $\frac{dx}{d\theta}= a\sec^{2} \theta$         |
| $\sqrt{ x^{2} - a^{2}}$ | $x=a\cosh u$     | $\frac{dx}{du}= a\sinh^{2} u$                  |
| $\sqrt{ x^{2} - a^{2}}$ | $x=a\sec \theta$ | $\frac{dx}{d\theta}= a\sec \theta \tan \theta$ |

### Circular functions
![[Pasted image 20211223092947.png]]

### Hyperbolic functions
![[Pasted image 20211223093006.png]]

### Examples
> Find $\int^{2}_{-2} \frac{\sqrt{x+2}}{x+6}\cdot dx$

$$\begin{align*}
\int^{2}_{-2} \frac{\sqrt{x+2}}{x+6}\cdot dx & &  u &= \sqrt{x+2}\\
& & u^{2}-2 &= x\\
& & 2u &= \frac{dx}{du}\\
&= \int^{2}_{0} \frac{u}{u^{2}+4}\cdot 2u \frac{du}{dx} dx\\
&= \int^{2}_{0} \frac{2u^{2}}{u^{2}+4}\cdot du
\end{align*}$$