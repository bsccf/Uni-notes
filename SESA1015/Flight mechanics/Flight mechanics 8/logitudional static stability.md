---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe and explain
## Logitudional static stability
### Intro

This is where you get [[static stability]] in the pitch axis of the aircraft, expressed mathamatically:

$$\begin{align*}
\frac{dC_{mG}}{d\alpha} &< 0 
\end{align*}$$
$dC_{mG}$ being the pitching moment about the centre of gravity
$\alpha$ being the [[Angle of attack]]

So to calculate this we will need an expression for $C_{mG}$ interms of $\alpha$. Introducing "maths":

### Maths
We will use the following diagram:

![[aircraft controls and dimentions for calculating longitudional stability#^267a4d]]

Now if we take moments about the centre of gravity:
$$\begin{align*}
 M_G &=  M_0 + L_W(h-h_0)c - P( l_T - (h-h_0)c )
\end{align*}$$
Here the $M_0 + L_W(h-h_0)c$ is from the wing and $- P( l_T - (h-h_0)c )$ is from the tailplane.

#### Desired diagram
So we can see by the equation that $P(...)$ is counteracting $L_W(...)$, which is desireable for static stability. But the important bit is how they change with changing $\alpha$ (angle of attack), to get an automatic return to the correct $\alpha$ we will need:
- $M_G<0$ when pitched upward
- $M_G>0$ when pitched downward

Hence:
- $M_0+L_W(...) < P(...)$ when pitched upward
- $M_0+L_W(...) > P(...)$ when pitched downward

![[Pasted image 20211206143540.png]]

#### Back to maths
Now we can convert everything into coefficients:
$$\begin{align*}
 \frac{M_G}{\frac{1}{2}\rho V^{2}S_c} &=  \frac{M_0 + L_W(h-h_0)c - P( l_T - (h-h_0)c )}{\frac{1}{2}\rho V^{2}S_c}\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \left(\frac{S_T l_T}{ Sc }\right)C_{LT}\\
& & \bar{V}&= \frac{S_T l_T}{ Sc }\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT}
\end{align*}$$

Note that $\bar{V}$ is known as the [[tail colume coefficient]].
We can use verticle equalibrium to simplify further $L=L_W+P=W=\frac{1}{2}\rho V^{2}SC_L$:
$$\begin{align*}
&&L&=L_W+P & W&=\frac{1}{2}\rho V^{2}SC_L\\
&&C_L &= C_{Lw} + C_{LT} \frac{S_T}{S}  &  \frac{2W}{\rho V^{2}S} &= C_L\\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_{Lw}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT} &C_L - C_{LT} \frac{S_T}{S}&= C_{Lw} \\
C_{mG} &=  C_{mo} + (h-h_0)\left(C_L - C_{LT} \frac{S_T}{S}+\frac{C_{LT}S_T}{S}\right) - \bar{V}C_{LT}\\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}C_{LT}
\end{align*}$$

Well now we have hit a wall, since we don't know how to determine $C_{LT}$, if only there was some sort of "[[tailplane lift coefficient|how do you determine the tailplane lift coefficient]]" document... wait that embeded?! Guess we have unhit said wall.

From [[tailplane lift coefficient]] we get:

![[tailplane lift coefficient#^d6f08f]]

Which we can now sub back:
$$\begin{align*}
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}C_{LT} & C_{LT} &= a_{1T} \alpha_T + a_{2T} \eta \\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}(a_{1T} \alpha_T + a_{2T} \eta) &&& \alpha_T &= \alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\\
C_{mG} &=  C_{mo} + (h-h_0)C_L - \bar{V}\left(a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) + a_{2T} \eta\right)\\
& & at\:C_{mG}&=0\\
0 &=  C_{mo} + (h-h_0)C_L - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) - \bar{V} a_{2T} \bar{\eta}\\
\bar{V} a_{2T} \bar{\eta} &=  C_{mo} + (h-h_0)C_L - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right)\\
\end{align*}$$

We now have a final resault for the elevator angle needed for trim:
> ### $$ \bar{V} a_{2T} \bar{\eta} =  C_{mo} + (h-h_0)C_L - \bar{V}a_{1T} \left(\alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S\right) $$ 
>> where:
>> $=$ 
>> $=$
>> $=$