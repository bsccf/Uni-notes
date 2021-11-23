---
aliases: ["minimum glide angle"]
tags: ["Question","QFormat3"]
---

#### What are the equations for
## Gliding without thrust
### Equation

> ### $$ \theta_{min} = 2 \sqrt{k C_{Do} } $$ 
>> where:
>> $\theta_{min}=$ [[gliding without thrust|minimum glide angle]]
>> $k=$ [[induced drag coefficient#^438b96|Another constant relating to wing shape]]
>> $C_{Do}=$ [[form drag coefficient]]

### Proof

![[Pasted image 20211123174004.png]]

$$\begin{align*}
   & & L &= W \cos \theta & D = W\sin\theta\\
\frac{D}{L} &= \frac{W\sin\theta}{W \cos \theta}\\
&= \tan \theta\\
\therefore \frac{D}{L}&\approx \theta \:\:\:small\:angle\:approx
\end{align*}$$

The glide angle will be a minimum when L/D ([[lift to drag ratio]]) is at a maximum. This will occur at [[calculating minimum drag|minimum drag]].

We know that [[calculating minimum drag|minimum drag]] occurs when: [[induced drag coefficient]] = [[form drag coefficient]] ($C_{Do}=C_{Di}$)

$$\begin{align*}
  \theta_{min} &= \frac{1}{{\left(\frac{D}{L}\right)_{min}}} & C_D &= C_{Di} + C_{Do} & C_{Di} &= k C_L^{2} & C_{Do} &= C_{Di}\\
 &= \frac{C_D}{C_L} & C_D &= 2 k C_L^2\\
 &= \frac{2 k C_L^2}{C_L}\\
&= 2 k C_L
\end{align*}$$

From [[lift coefficient at min drag]]:
$$\begin{align*}
   \theta_{min} &= 2 k C_L & C_{LminD} =& \sqrt\frac{C_{Do}}{k} & k&=\frac{K}{\pi A}\\
\theta_{min} &= 2 k \sqrt\frac{C_{Do}}{k}\\
\theta_{min} &= 2 \sqrt{k C_{Do} }
\end{align*}$$
