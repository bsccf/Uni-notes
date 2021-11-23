---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Minimum power speed
Power is the rate of doing work, we know that $P=Fv$ so applieing that to drag knowing that drag = thrust:

![[calculating minimum drag#^fb4ad2]]

$$ \begin{align*}
P &= DV \\
&= ( A'V^{2} + \frac{B'}{V^{2}} )V\\
&= A'V^{3} + \frac{B'}{V}\\
\frac{dP}{dV} &= 3A'V^{2} - \frac{B'}{V^2}\\
& & \frac{dP}{dV} &= 0\\
0&=3A'V^{2} - \frac{B'}{V^2}\\
\frac{B'}{V^2}&=3A'V^{2} \\
\frac{B'}{3A'}&=V^{4}\\
V&=\sqrt[4]\frac{B'}{3A'}
\end{align*} $$

If we refer to [[min drag speed in steady level flight]]:

$$ \begin{align*}
V_{MP} &=\sqrt[4]\frac{B'}{A'} \cdot \sqrt[4] \frac{1}{3}\\
V_{MP} &= V_{MD} \cdot \sqrt[4] \frac{1}{3} \approx V_{MD} \cdot 0.76
\end{align*} $$

So:
> $$ V_{MP} = V_{MD} \cdot \sqrt[4] \frac{1}{3} \approx V_{MD} \cdot 0.76 $$ 
>> where:
>> $V_{MP}=$ Speed at minimum power
>> $V_{MD}=$ [[min drag speed in steady level flight]]

^6d5ee2

Hence the min power speed is less than the min drag speed.

### Relationships at min power speed

At the minimum power speed all the following are true:

#### Induced drag and form drag

> ### $$ 3 C_{Do} = k C_L^2 $$ 
>> where:
>> $C_{Do}=$ [[form drag coefficient]]
>> $k=$ [[induced drag coefficient#^438b96|constant related to wing shape]]
>> $C_L=$ [[Lift coefficient]]

^0cb1a3

#### Lift to drag ratio
> ### $$ \frac{L}{D}_{minP} = \frac{3C_L}{4C_{Do}} = \frac{1}{4kC_L} $$ 
>> where:
>> $\frac{L}{D}_{minP}=$ [[lift to drag ratio]] at min power
>> $C_{Do}=$ [[form drag coefficient]]
>> $k=$ [[induced drag coefficient#^438b96|constant related to wing shape]]
>> $C_L=$ [[Lift coefficient]]
