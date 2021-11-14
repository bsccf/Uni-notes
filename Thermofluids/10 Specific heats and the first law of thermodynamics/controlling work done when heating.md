---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What's the theory behined
## Controlling work done when heating
### Intro
When working with heating this fact should be kept in mind:
![[equation for change in internal energy]]

So to effectively heat something with the goal of increasing temperature, you want to maxamise the change in [[internal energy]] while minamising the work done by the system. (sometimes the opposite may also be true, depending on requirements ofc)
![[kid_sets_his_fucking_hand_on_fire.mp4]]

### Volume changes and work done
We know according to the [[ideal gas law]] that if you increase somethings temperature then it's pressure or volume will also increase ($\frac{pV}{T}=k$) but when a container expands whether that be in something like a baloon or a piston work is done to expand that volume, this work done decreases the energy that goes into heating the substance.

#### Heating at constant volume
So if you instead heat something at a constant volume in a sealed container then no work is done on the container ($E=Fx$) with no change in distance no work can be done. Hence more of the [[heat]] is used to increase internal energy and hence temperature.

#### Gas internal energy
If we now do some more detailed math to express this:
$$\begin{align*}
  E_u &=\frac{3}{2}Nk_B T\\
 &= \frac{3}{2} k_B T\\
&= \frac{3}{2} mRT\\
&= m C_V T\\
e_u &=C_V T
\end{align*}$$
$\therefore e_u =C_V T$ is only true for atoms.

### Constant pressure and work done

$$\begin{align*}
   \frac{pV}{T} &= k & E&=F\Delta x & F &= pA & \Delta x &= \frac{\Delta V}{A} \\
\frac{p (V+\Delta V)}{(T+\Delta T)} &= k & &=pA\Delta x \\
p (V+\Delta V) &= k (T+\Delta T) &   &= pA\frac{\Delta V}{A}\\
 \Delta V &= \frac{k}{p} (T+\Delta T) - V & &= p\Delta V\\
& & &= p\left( \frac{k}{p} \left(T+\Delta T\right)-V \right)
\end{align*}$$