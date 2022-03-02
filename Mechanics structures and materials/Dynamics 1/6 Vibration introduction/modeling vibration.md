---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the mathamatical method for
## Modeling vibration
In the tutorial they start with free oscillation then move onto damped oscillation, that's [[it really is though|kinda cringe]] so I'm going to do it in the opposite order.









### Proof
First lets get a diagram representing some mass on a spring of negligible mass:
![[Pasted image 20220302112318.png]]

Each of the forces are:
- $T(x,\dot{x},\ddot{x}, ...)=$ Some tension force function
- $D(x,\dot{x},\ddot{x}, ...)=$ Some drag force function
- $mg=$ Weight

Now this isn't very helpfull, so we can use simple models for drag and tension:
- $T=k(x+Q)$
- $D=c\dot{x}$ where $c$ is some constant

The displacement $Q$ is the value needed for tension and weight to be equal when $\dot{x}=0,x=0$:
$$\begin{align*}
T + D &= mg\\
k(x+Q) + c\dot{x} &= mg & let:&\:x=0,\:\dot{x}=0\\
k(Q) &= mg\\
Q &= \frac{mg}{k}
\end{align*}$$


