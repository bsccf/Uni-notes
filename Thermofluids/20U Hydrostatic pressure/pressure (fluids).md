---
aliases: ["pressure"]
tags: ["Question","QFormat3"]
---

#### What is
## Pressure (fluids)
### Equations
The pressure due to the weight of the above an uncompressible fluid column can be determined using:
> ### $$ p = h\rho g $$ 
>> where:
>> $p=$ [[pressure (fluids)]]
>> $h=$ hight of column
>> $\rho=$ density of fluid
>> $g=$ gravity

For uncompressible fluids you can take $\rho$ as constant, but for gases you might need to be more creative, this form should work:
> ### $$ d p = \rho(h) \times  g(h) \times d h $$ 
>> where:
>> $p=$ [[pressure (fluids)]]
>> $h=$ hight of column
>> $\rho(h)=$ density of fluid as a function of h
>> $g(h)=$ gravity as a function of h

### Example
If we wanted to model the pressure in atmosphere at some hieght we could use the [[ideal gas law]] as well as the second version of this equation:

To make things easy I'm going to assume:
- Constant gravity
- Constant temperature
- Constant atmospheric composition
- Ideal gas law is valid

$$\begin{align*}
& & pV &= mRT\\
dp &= \rho g dh & \frac{p}{RT} &= \rho\\
\int 1 \cdot dp &= \int \frac{p}{RT} g \cdot dh\\
\int \frac{1}{p} \cdot dp &= \int \frac{1}{RT} g \cdot dh
\end{align*}$$
Now if we can define column hieght $h_P=H_{0}-H$ at pressure $P$, and then pressure for the entire column height to be a hieght of $H_0$ and pressure of $P_0$:
$$\begin{align*}
\int^{P_0}_{P} \frac{1}{p} \cdot dp &= \int^{H_0}_{H_0-H} \frac{1}{RT} g \cdot dh\\
[ \ln(p) ]^{P_0}_{P} &= [\frac{gh}{RT}]^{H_0}_{H_0-H}\\
\ln({P}) - \ln(P_{0})&= \frac{g}{RT}(H_0-H-H_0)\\
ln\left(\frac{P}{P_{0}}\right)&= -\frac{Hg}{RT}\\
\frac{P}{P_{0}}&=e^{-\frac{Hg}{RT}}\\
P&=P_{0} \times e^{-\frac{Hg}{RT}}
\end{align*}$$
And now you have an equation that (poorly) models the density of the atmosphere above some refrence pressure. 