---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating aircraft range
### Maths
#### Setting it up
We know:

![[specific fuel consumption (aircraft)#^1d3da2]]

$$\begin{align*}
   \frac{dW}{dt} &= -sT\\
& & W=&T & L=&W\\
\frac{dW}{dt} &= -sD &   &  &  1=&\frac{W}{L}\\
\therefore \frac{dW}{dt} &= -s \frac{WD}{L}\\
\end{align*}$$

Also:

$$\begin{align*}
  \frac{dW}{dt}  &= \\
&= \frac{dW}{dx} \frac{dx}{dt}\\
\therefore \frac{dW}{dt} &= \frac{dW}{dx} V
\end{align*}$$

Equating these two resaults:

$$\begin{align*}
   \frac{dW}{dx} V &= -s \frac{WD}{L}\\
\frac{dW}{dx} &= - \frac{s}{V} \frac{D}{L}W
\end{align*}$$

We now have an equation relating the rate of change of weight over distance, assuming that $\frac{s}{V}$ and $\frac{D}{L}$

#### Integration time
