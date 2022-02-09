---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the equation and theory assosiated with
## Conservation of energy in flow
### Intro

Apply "energy can't be created or destroyed" to flow, there you go... you now know the theory!

([[idk stuff|yes that's it]])

### Proof

![[Pasted image 20220209183106.png]]

Here I'm using $A_{0}$ as the refrence point and $A$ to represent any cross sectional position, in reality $A_{0}$ is just as arbritry as $A$ and they both can be any cross section of the shape that has stuff flowing through it, I just like these letters [>\_<]. 

First we define the current potential energy of the fluid at the two points, this consists of it's pressure, gravitational and kinetic energy:

$$\begin{align*}
dE_{0} &= \frac{1}{2}dm_{0} U_{0}^{2} + h_{0} dm_{0} g + P_{0} V & &... \\
dE_{0} &= dm_{0}\left(\frac{1}{2} U_{0}^{2} + h_{0} g\right) + P_{0} V & &... \\
dE_{0} &= A_{0} dx_{0} \rho_{0}\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} dx_{0} & &... \\
& & dE &= A dx \rho\left(\frac{U^{2}}{2}  + h g\right) + PA dx
\end{align*}$$

We can then apply conservation of energy between the two points (I'm using $dF$ for frictional losses)

$$\begin{align*}
dE + dF &= dE_{0}\\
A dx \rho\left(\frac{U^{2}}{2}  + h g\right) + PA dx + dF &= A_{0} dx_{0} \rho_{0}\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} dx_{0}\\
\end{align*}$$

This is becomeing nasty quickly and I haven't even subbed in [[conservation of mass in flow#^4e4ed8]] (I also assumed $g=g_{0}$ which isn't nessisar), so instead of a version that's valid for variable density ect I am going to be using the following assumptions from here on:
- The fluid is non compressible and uniform density
- There are no frictional forces within the pipe
- There is no change of mass within the pipe

Now lets use the [[conservation of mass in flow#^90d47a|non cancerous version of the conservation of mass formula thing]] and other stuff:

$$\begin{align*}
A dx \rho\left(\frac{U^{2}}{2}  + h g\right) + PA dx + dF &= A_{0} dx_{0} \rho_{0}\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} dx_{0}\\
A dx \rho\left(\frac{U^{2}}{2}  + h g\right) + PA dx  &= A_{0} dx_{0} \rho\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} dx_{0}\\
A \frac{dx}{dt} \rho\left(\frac{U^{2}}{2}  + h g\right) + PA \frac{dx}{dt}  &= A_{0} \frac{dx_{0}}{dt} \rho\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} \frac{dx_{0}}{dt} & AU &= A_{0}U_0 \\
A_{0}U_0 \rho\left(\frac{U^{2}}{2}  + h g\right) + PA_{0}U_0  &= A_{0} U_0 \rho\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} A_{0} U_{0}\\
 \rho\left(\frac{U^{2}}{2}  + h g\right) + P  &=  \rho\left(\frac{U_{0}^{2}}{2}  + h_{0} g\right) + P_{0} \\
\frac{\rho U^{2}}{2}  + \rho h g + P  &=  \frac{\rho U_{0}^{2}}{2}  + \rho h_{0} g+ P_{0} 
\end{align*}$$