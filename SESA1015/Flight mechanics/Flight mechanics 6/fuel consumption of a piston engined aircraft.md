---
aliases: ["specific fuel consumption (engine)"]
tags: ["Question","QFormat3"]
---

#### What is the
## Fuel consumption of a piston engined aircraft
### Introduction
Unlike jets that use [[specific fuel consumption (aircraft)]], piston engines have their sfc measured in different units:
- sfc (aircraft), $Newtons(Fuel)/Second\cdot Netwon(Thrust)$
- sfc (engine), $Newtons(Fuel)/Second \cdot Power$

So now to get fuel per second to thrust per second we need to covert power to thrust, this is done through a propeller.

> ### $$ \frac{dW(t)}{dt} = -Ps' $$ 
>> where:
>> $\frac{dW(t)}{dt}=$ Weight of fuel change per second 
>> $P=$ Power
>> $s'=$ [[fuel consumption of a piston engined aircraft|specific fuel consumption (engine)]]

### Converting to thrust
Though the form above is pretty useless, so we can convert it to a more useful form by converting power into thrust.

![[propeller combined efficiency]]

We know that to maintain a steady speed drag=thrust and P=Fv so $P=DV$, subbing that into the equations:

$$\begin{align*}
  & & \eta P' &= P & P &= DV\\
\frac{dW(t)}{dt} &= -P's' &  P' &= \frac{P}{\eta}\\
\frac{dW(t)}{dt} &= -\frac{P}{\eta}s'\\
\frac{dW(t)}{dt} &= -\frac{DV}{\eta}s' & 1=\frac{W}{L}\\
\frac{dW(t)}{dt} &= -\frac{DV}{\eta}s'\cdot\frac{W}{L}\\
\frac{dW(t)}{dt} &= -V\frac{s'}{\eta}\cdot\frac{WD}{L}\\
\frac{dW(t)}{dt} &=- \frac{dx}{dt}\frac{s'}{\eta}\cdot\frac{WD}{L}\\
-\int \frac{L}{WD}\frac{\eta}{s'} dW &=\int 1 dx\\
-\frac{\eta}{s'}\cdot\frac{L}{D}\int \frac{1}{W}  dW &=\int 1 dx\\
-\frac{\eta}{s'}\cdot\frac{L}{D} \ln(W) + k  dW &= R\\
R &= \frac{\eta}{s'}\frac{L}{D}\cdot \ln\left( \frac{W_1}{W_2} \right)
\end{align*}$$

### Conclusion
This is known as the [[Breguet range equation (piston engine)]] but for propeller aircraft:
![[Breguet range equation (piston engine)]]

