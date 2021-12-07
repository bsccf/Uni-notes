---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find
## Shear stress in a beam cross section


### Proof
#### Getting expressions for the left and right sides
To find the shear stress at a specific point we are going to have to do some maeth, consider the following:
![[Pasted image 20211207232317.png]]
You can see that:
$$\begin{align*}
M_{left} &= M & M_{right} &= M + \frac{dM}{dx}dx 
\end{align*}$$


#### things
Now remember how we showed in previous notes that $Q$ at any point along a beam could be expressed by starting from one side and moving to the other (see [[method for constructing shear force and bending moment diagrams]]), basically we are going to employ a simular method to calculate the sum of the shear forces on a cut face starting from the bottom:
![[Pasted image 20211207233037.png]]

First lets use this diagram and the privous s We know that the stress at a given point along the face is given in [[engineer's bending theory]]:
![[engineer's bending theory#^6fb9ef]]

So we can determine the left and right stresses:
$$\begin{align*}
Left : \sigma_{xx} &= \frac{My}{I} & Right: \sigma_{xx}+ \frac{\Delta \sigma_{xx}}{\Delta x} dx= \left(M+ \frac{dM}{dx} dx\right) \frac{y}{I}
\end{align*}$$
