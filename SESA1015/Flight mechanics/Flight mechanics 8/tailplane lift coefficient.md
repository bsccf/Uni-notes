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
and\: \frac{w}{V} &\approx costant\\
\therefore \tan \varepsilon&\approx constant
\end{align*}$$

We know that (tailplane angle of attack) $=\alpha_T = \alpha+\alpha_S - \varep$