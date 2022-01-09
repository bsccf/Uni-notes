---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Modelling forced elastic systems expereincing oscillation
[[insert funny message here|tldr]], you get the [[modelling oscillations of damped elastic systems using constant-coefficient differential equations|equation for modelling oscillating systems]] and add some thing onto it then use methods from [[general solution of linear nonhomogeneous constant coefficient equations]].

### Intro
Basically this is where you have some oscillating system that has some extra driving force acting on it. There are some definitions you should probably be aware of:
- [[free vibrations]]
- [[forced vibrations]]

### Example
So if we model a lamp post vibrating in the wind:
![[Pasted image 20220109122644.png]]
Using a bunch of assumptions are rearrangements as described [[Pasted image 20220109122742.png|here]] we get the equation:

$$ \frac{d^{2}x}{dt^{2}} + 2\zeta \omega \frac{dx}{dt} + \omega^{2}x = F\cos\Omega t $$

Now it's just following the method in [[general solution of linear nonhomogeneous constant coefficient equations]]:
