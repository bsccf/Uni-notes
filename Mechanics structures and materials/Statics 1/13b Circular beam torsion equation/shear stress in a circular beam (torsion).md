---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you model
## Shear stress in a circular beam (torsion)

### Proof
Note we are still assuming that the beam doesn't expand latterally due to torsion, this is clearly false but considering how little it does change dimentions is a resonable assumption especially with how much it simplifies the maths.
Continueing with the diagram from [[shear strain in a circular beam (torsion)]]:

![[Pasted image 20211207122420.png]]

If we focus on shear stress it looks like:

![[Pasted image 20211207124320.png]]

Where $\tau$ is the shear stress. Now we can relate that to [[shear strain in a circular beam (torsion)]] using the [[shear modulus]].

$$\begin{align*}
G &= \frac{\tau}{\gamma}  & \gamma &= \frac{R\theta}{L}\\
G &= \frac{\tau}{\frac{R\theta}{L}}\\
\therefore \frac{GR\theta}{L} &= \tau
\end{align*}$$

But so far we have been focusing on the outermost surface of the cylinder