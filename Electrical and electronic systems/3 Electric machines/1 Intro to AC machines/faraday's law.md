---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Faraday's law
Faraday's law of induction is a basic law of electromagnetism predicting how a [[magnetic field]] will interact with an electric circuit to produce an [[electromotive force]] ([[electromotive force|EMF]])—a phenomenon known as electromagnetic induction. 
It is the fundamental operating principle of transformers, inductors, and many types of electrical motors, generators and solenoids. ([[kinda the backbone of modern human civilization no big deal|so useful]])

It states "The [[electromotive force]] around a closed path is equal to the negative of the time rate of change of the [[magnetic flux]] enclosed by the path."
Or put as an equation for a single coil of wire:

> ### $$ \mathcal {E} = - \frac{d\phi}{dt} $$ 
>> where:
>> $\mathcal {E}=$ [[electromotive force|EMF]]
>> $\phi=$ [[magnetic flux]]
>> $t=$ time

Alternatively for a tightly wound coil of wire:

> ### $$ \mathcal {E} = - N \frac{d\phi}{dt} $$
>> where:
>> $\mathcal {E}=$ [[electromotive force|EMF]]
>> $\phi=$ [[magnetic flux]] through a single loop
>> $t=$ time
>> $N =$ identical turns of the wire
> 
> (I'm pretty sure that [[flux linkage]] can also be used, so $\mathcal {E} = - \frac{d\lambda}{dt}$ )

### Useful form

What's important to understand is that it is the flux enclosed by the loop, so in a uniform magnetic field it is proportional to AREA in the loop!

Another form (more useable):

![[Pasted image 20220203173926.png]]

> ### $$ \mathcal {E} =- NBLu $$ 
>> where:
>> $\mathcal {E}=$ [[electromotive force|EMF]]
>> $N=$ identical turns of the wire
>> $B=$
>> $L=$

[[UNFINISHED STUFF]]

Take a look at the following diagram, you don't need to care about the [[Lorentz's force law|lorentz force]] or current right now all that's important is $\alpha, D, L$. If we assume the [[tesla|magnetic flux density]] to be constant between the magnets which is generally a resonable approximation inside many electronic machines then:
- We know the area inside the loop is: $A=LD$.
- We know that [[magnetic flux]] is measured using the normal component to the surface, so at $\alpha=0$ flux is at a maximum and at $\alpha=\frac{\pi}{2}$ flux is zero. So the perpendicular component of flux can be defined as: $\phi=AB\cos\alpha$ where $B$ is [[tesla|magnetic flux density]]
- We can also define $\alpha$ interms of angular velocity as $\alpha=t\omega$
- Finally from [[faraday's law]]: $\mathcal {E} = - \frac{d\phi}{dt}$
Now we can sub all this together:
$$\begin{align*}
\mathcal {E}& = - \frac{d\phi}{dt} & \phi&=AB\cos\alpha & \alpha&=t\omega & A&=LD\\
& & &=LD\cos(t\omega)\\
& & \frac{d\phi}{dt} &=-LDB \omega \sin(t\omega)\\
\mathcal {E}& = LDB \omega \sin(t\omega)
\end{align*}$$

Now if we imagine lots of these loops tightly wound ontop of eachother, call the number of loops $N$, the total area becomes $A=NLD$ so our final equation would then become:
$$\begin{align*}
\mathcal {E}& = NLDB \omega \sin(t\omega)
\end{align*}$$