---
aliases: ["fibre reinforced composite"]
tags: ["Question","QFormat3"]
---

#### What are
## Fibre reinforced composites
### Basics
These are [[composites]] that use fibres as [[reinforcement (materials)|reinforcement]].

![[Pasted image 20211215162033.png]]

### Mechanics
#### Graphical analysis
![[Pasted image 20211215162305.png]]
The stress strain relationship of a [[composites|composite]] will generally lie somewhere inbetween the line of the [[matrix (materials)|matrix]] and the [[reinforcement (materials)|reinforcement]].

#### Directional behaviour
As you can imagine the behaviour under stress will vary directionally assuming the threads are aligned in specific directions. If we take the following example we can model it's behaviour under stress:
![[Pasted image 20211215162531.png]]

##### Longitudinal loading
Here if we start by assuming a good interface between the fibre and matrix we can assume that strains are all the same:
$$\begin{align*}
F_c &= F_m + F_f \\
\sigma_c A_c &= \sigma_m A_m + \sigma_f A_f && & E &= \frac{\sigma}{\varepsilon}\\
E_c\varepsilon_c A_c &= E_m\varepsilon_m A_m + E_f\varepsilon_f A_f & \varepsilon_c &= \varepsilon_m = \varepsilon_f\\
E_c A_c &= E_m A_m + E_f A_f &&& V &\propto A\\
E_c V_c &= E_m V_m + E_f V_f & V_c &= V_m + V_f\\
E_c &= \frac{E_m V_m + E_f V_f}{V_m + V_f}\\
&
&\end{align*}$$