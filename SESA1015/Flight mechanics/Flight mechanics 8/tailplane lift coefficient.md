---
aliases: ["how do you determine the tailplane lift coefficient"]
tags: ["Question","QFormat3"]
---

#### How do you determine the
## Tailplane lift coefficient ($C_{LT}$)
### Intro
The tailplane is kinda annoying, because when positioned behined the main wing it ends up recieving the main wings downwash. So the air comes at it with an akward angle, which we need to account for.
![[Pasted image 20211206151547.png]]

### Math
![[tailplane airflow dimensions#Tailplane airflow dimensions]]

Lets first determine the downwash angle at the tailplane:

$$\begin{align*}
 \tan \varepsilon &= \frac{w}{V} \approx \varepsilon\\
\frac{w}{V} &\approx constant\times \frac{C_L}{\pi A} & \alpha \propto C_L \\
\therefore \varepsilon&\approx constant \times \alpha\\
\therefore \frac{d\varepsilon}{d\alpha} & \approx constant\\
\end{align*}$$

(note $\alpha \propto C_L$ is from [[effect of angle on lift coefficient]])

Note that $\frac{d\varepsilon}{d\alpha}$ is the variation of the downwash angle with angle of attack, common values for this are between 0.2 and 0.5, depending on tailplane position.

We know that (tailplane angle of attack) $=\alpha_T = \alpha+\alpha_S - \varepsilon$:
$$\begin{align*}
\alpha_T &= \alpha+\alpha_S - \varepsilon & \varepsilon = \frac{d\varepsilon}{d\alpha} \alpha\\
&= \alpha+\alpha_S - \frac{d\varepsilon}{d\alpha} \alpha\\
\therefore \alpha_T &= \alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S
\end{align*}$$

Next we will use an equation that we don't need to prove:

> ### $$ C_{LT} = a_{1r} \alpha_T + a_{2e} \eta $$ 
>> where:
>> $C_{LT}=$ [[tailplane lift coefficient]]
>> $a_{1r}= \dfrac{dC_{LT}}{d\alpha_T}=$ lift curve slope of tailplane (for a constant value of $\eta$) 
>> $a_{2r}= \dfrac{dC_{LT}}{d\eta}=$ constant (for a value constant of $\alpha_T$)
>> $a_T = \alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S$

> ### $$ C_{LT} = a_{1r} \alpha_T + a_{2e} \eta $$ 
>> where:
>> $C_{LT}=$ [[tailplane lift coefficient]]
>> $a_{1r}= \dfrac{dC_{LT}}{d\alpha_T}=$ lift curve slope of tailplane (for a constant value of $\eta$) 
>> $a_{2r}= \dfrac{dC_{LT}}{d\eta}=$ constant (for a value constant of $\alpha_T$)
>> $a_T = \alpha\left(1 - \frac{d\varepsilon}{d\alpha}\right)+\alpha_S$