---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Constant altitude and angle of attack [[cruise pattern]] (jet)
Unlike the [[cruise climb with constant speed|the other technique]] we encountered this one involves varying the speed and maintaining the same altitude.

### Assumptions
The angle of attack is constant and the altitude is constant:
- $L/D=$ constant (angle of attack is constant)
- $\rho=$ constant (altitude is constant)

Hence since:
$$\begin{align*}
  W = L &= \frac{1}{2}\rho V^{2}S C_L
\end{align*}$$
We must be varying the speed to control lift as weight changes, so $V=\sqrt\frac{2W}{\rho S C_L}$

### Maths time
We know from [[specific fuel consumption (aircraft)|specific fuel consumption]]:
$$\begin{align*}
   \frac{dW}{dt} = -sT &= -sD\\
\therefore \frac{dW}{dx} \frac{dx}{dt} = \frac{dW}{dx}V &=
\end{align*}$$
$$\begin{align*}
   \frac{dW}{dx}V &= -sD & V=&\sqrt\frac{2W}{\rho S C_L} & D &= \frac{1}{2}V^{2}SC_D \\
\frac{dW}{dx} &= -s\frac{1}{2}V^{2}SC_D\\
&= -s\frac{1}{2}VSC_D\\
&= -\frac{s \cdot SC_D}{2} \sqrt\frac{2W}{\rho S C_L}\\
\int 1 \cdot dx &= -\int \frac{2}{s \cdot SC_D} \sqrt\frac{\rho S C_L}{2W} \cdot dW\\
x &= -\frac{2}{s \cdot SC_D} \cdot \sqrt{ \frac{\rho S C_L}{2} } \int  \sqrt\frac{1}{W} \cdot dW\\
&= -\frac{1}{s C_D} \cdot \sqrt{ \frac{2\rho C_L}{S} } \int  \frac{1}{\sqrt W} \cdot dW\\
&= -\frac{1}{s C_D} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot 2\ln(\sqrt W) + c \\\\
&= \frac{2}{s C_D} \cdot \sqrt{ \frac{2\rho C_L}{S} } \cdot \ln\left(\sqrt {\frac{W_s+W_f}{W}}\right)
\end{align*}$$