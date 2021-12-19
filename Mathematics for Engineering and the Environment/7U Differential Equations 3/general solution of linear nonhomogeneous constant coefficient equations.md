---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find the
## General solution of linear nonhomogeneous constant coefficient equations







### Example

> Find the general solution of $\frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x = t^{2}$

First we need a [[particular integral]], so we try something suitable, lets try $x(t)=Pt^{2} + Qt + R$

$$\begin{align*}
&&x &= Pt^{2} + Qt + R\\
&&\frac{dx}{dt} &= 2Pt + Q\\
t^{2} &= \frac{d^{2}x}{dt^{2}} + 5\frac{dx}{dt} - 9x & \frac{d^{2}x}{dt^{2}} &= 2P\\
 &= (2P )+ 5(2Pt + Q) - 9(Pt^{2} + Qt + R)\\
 &= 2P + 10Pt + 5Q - 9Pt^{2} - 9Qt - 9R\\
 0 &= t^{2} ( -1 - 9P ) + t( 10P - 9Q ) + ( 2P + 5Q - 9R )\\
& & 1 &= 9P & 0 &= 10P - 9Q & 0 &= 2P +5Q - 9R\\
&& -\frac{1}{9} &= P & \frac{10P}{9} &= Q & \frac{2P +5Q}{9} &= R\\
&& &&  -\frac{10}{81}&=Q\\
&& && &&  - \frac{68}{729} &=R \\
\therefore x(t)&=-\frac{1}{9}t^{2} -\frac{10}{81} t - \frac{68}{729} \\& is \:the\:particular\:integral
\end{align*}$$

We now need to find the [[complementary function]], we can do this using [[integra]]