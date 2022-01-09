---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Modelling oscillations of damped elastic systems using constant-coefficient differential equations

### Intro
So if your lazy and want to model a pendulum you can assume no frictional forces are acting on it, then you can use a diagram such as the following:
![[Pasted image 20220109103318.png]]
And create an equation like:
$$ ml \frac{d^{2}\theta}{dt^{2}} = - mg\sin \theta $$
But this equation predicts motion that is perpetual, which is... well not realistic. So we usually slap in a funtion R, where R is the acceleration due to air resistance:
![[Pasted image 20220109103450.png]]
$$  ml \frac{d^{2}\theta}{dt^{2}} = -R - mg\sin \theta  $$
Now this is where people start to do their own thing, R can be modelled in a bunch of ways if you recall [[Drag equation|the drag equation]] models it as $V^2$, though at low speeds drag is basically just a constant, another approach would be to say $R(V)=Vk$ and just model it as being proportional to V, this is the mathamatical equivilent of "if one increases the other does too, [[lazyness is alwayse the answer|cba]] lets just say they're proportional"