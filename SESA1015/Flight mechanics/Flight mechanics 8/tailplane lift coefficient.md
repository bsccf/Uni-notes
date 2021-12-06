---
aliases: ["how do you determine the tailplane lift coefficient"]
tags: ["Question","QFormat3"]
---

#### How do you determine the
## Tailplane lift coefficient
### Intro
The tailplane is kinda annoying, because when positioned behined the main wing it ends up recieving the main wings downwash. So the air comes at it with an akward angle, which we need to account for.
![[Pasted image 20211206151547.png]]

### Math
![[tailplane airflow dimensions#Tailplane airflow dimensions]]

Lets first determine the downwash angle at the tailplane:

$$\begin{align*}
 \tan \varepsilon &= \frac{w}{V} \approx \varepsilon\\
\frac{w}{V} &\approx constant\times \frac{C_L}{\pi A} & \alpha \propto C_L \\
\therefore \varepsilon&\approx constant \times \alpha
\end{align*}$$

(note $\alpha \propto C_L$ is from [[effect of angle on lift coefficient]])

We know that (tailplane angle of attack) $=\alpha_T = \alpha+\alpha_S - \varepsilon$:
$$\begin{align*}
\alpha_T &= \alpha+\alpha_S - \varepsilon\\
&= \alpha+\alpha_S - \varepsilon
\end{align*}$$