---
aliases: ["thrust limit"]
tags: ["Question","QFormat3"]
---

#### What is the
## Limit on the thrust during a co-ordinated turn
### Intro
For everything so far we have basically just been assuming that the engines can keep up, but here's a real shocker... engines can't output infinate thrust.
So thrust becomes a limiting factor.

This especially becomes an issue when you consider that during a [[co-ordinated turn]] lift tends to exceed weight, with higher turns having even higher lifts required.
(as we know drag tends to increase with lift due to its [[induced drag coefficient]] component).

### Math time
Lets just assume we have a term called $T_{max}$, which is the max thrust the aircraft can produce.

$$\begin{align*}
T_{max} &= D & D&=\frac{1}{2}\rho V^{2} S C_D & C_D &= C_{Do} + kC_L^{2} & R_{min}&= \frac{V^{2}}{g} \frac{1}{\sqrt{ \left(\frac{L_{max}}{W}\right)^{2} - 1}} \\
&= \frac{1}{2}\rho V^{2} S (C_{Do} + kC_L^{2}) &&&&& \frac{V^{2}}{gR_{min}} &= \sqrt{ \left(\frac{L_{max}}{W}\right)^{2} - 1} \\
&= \frac{1}{2}\rho V^{2} S C_{Do} + \frac{1}{2}\rho V^{2} S kC_L^{2} & L &= \frac{1}{2}\rho S V^{2} C_L &&& W\sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1} &= L_{max}\end{align*}$$
Ok it's become so phat that I need to shift it:
$$\begin{align*}
T_{max} &= \frac{1}{2}\rho V^{2} S C_{Do} + WkC_L\sqrt{\left(\frac{V^{2}}{gR_{min}}\right)^{2} + 1} \\
&
\end{align*}$$
