---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you calculate
## Centre of force on a flat wall
### Equation
General form, this would work for walls with variable thickness and variable pressures:

> ### $$ 0 = \int^{H}_{0} h p(h) \times w(h) - h_{c} p(h) \times w(h) \cdot dh $$ 
> ### $$ 0 =  \int^{H}_{0} (h - h_{c}) \times p(h) \times w(h) \cdot dh $$ 
>> where:
>> $H=$ vertical height of the wall where the force acts over
>> $h=$ vertical hieght postion (remember you may need to adjust formula when working with angled surfaces)
>> $h_c=$ h position of centre of force
>> $p(h)=$ pressure as a function of verticle hieght
>> $w(h)=$ pressure as a function of verticle height

Simplified form that takes in [[pressure (hydrostatics)#^07ca11]] as its function of pressure and assumes constant thickness:

> ### $$ h_{c} = \frac{2}{3}H $$ 
>> where:
>> $H=$ vertical height of the wall where the force acts over
>> $h=$ vertical hieght postion (remember you may need to adjust formula when working with angled surfaces)
>> $h_c=$ h position of centre of force

### Proof
I don't have access to a proper diagram making program rn so cope with this:
![[Pasted image 20220115100328.png]]
It is important to note that for all this working I don't need to consider $\alpha$ because [[pressure (hydrostatics)|pressure]] acts at the normal of surfaces, and all my functions work with verticle height which basically means that I'm leaving all the annoying conversions to the pleb thats unfortionate enough to neet these equations:

$$\begin{align*}
0&= \int^{-h_{c}}_{H-h_{c}} xwp\cdot dx &x &= h - h_{c} \\ 
& &h &= x + h_{c}& \frac{dh}{dx} &= 1\\
& &&& dh &= dx\\
0&= \int^{0}_{H} (h-h_{c})wp\cdot dh
\end{align*}$$
Then you can sub in $$