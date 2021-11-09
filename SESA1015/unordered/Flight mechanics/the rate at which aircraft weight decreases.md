---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you get
## The rate at which aircraft weight decreases
### Introduction
Unless you are drone striking an orphanage the only reason your plane should really be loosing weight is through fuel consumption, and here's a real shocker fuel consumption is determined by... engines. (atleast I hope so)

So we need a nice way of expressing fuel consumption interms of thrust, to do this we use [[specific fuel consumption (aircraft)]].

![[specific fuel consumption (aircraft)]]

### When in equalibrium
Well we know that:
- Thrust = Drag
- Lift = Weight

So lets sub that into out [[specific fuel consumption (aircraft)|s.f.c]] equation, we will also be using: [[lift to drag ratio]]

$$\begin{align*}
  \frac{dW(t)}{dt}  &= -sT\\
&= -sD\\
&= -s \frac{D}{L}L\\
&= -s \frac{D}{L}W & \frac{L}{D} &= \frac{C_L}{C_D} \\
&= -s \frac{C_D}{C_L}W
\end{align*}$$

Hence:
