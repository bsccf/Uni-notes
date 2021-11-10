---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating aircraft fuel at a given time
### Introduction
#### Rate of change
To calculate the fuel at a given time we need to know the rate at which fuel is used as well as starting fuel, luckily we already found the first part:

![[the rate at which aircraft weight decreases#^5a7c77]]

#### Weight
In reality the weight of the aircraft isn't just fuel, it also contains "aircraft bits" (that's the technical term) and sometimes valuble cargo such as the cocane bricks hidden inside the chairs. So for this we need to describe what makes up the aircrafts weight:

![[weight of an aircraft]]

### Maths
Now we have starting conditions defined and rate of change, you can guess what comes next. Intergration! (fun)

$$\begin{align*}
    \frac{dW}{dt} &= -sW \frac{C_D}{C_L}\\
\int \frac{1}{W} dW &= -s \frac{C_D}{C_L} \int  1 dt\\
\ln(W) &= -s \frac{C_D}{C_L} (t + k)\\
-\ln(W)\frac{C_L}{sC_D}+ k &= t \\
-\ln(W)\frac{C_L}{C_D} \frac{1}{s}+ k &= t & at\:t=0,\:\:\: k=&W=W_s+W_f\\
-\ln(W)\frac{C_L}{C_D} \frac{1}{s}+W&=
\end{align*}$$