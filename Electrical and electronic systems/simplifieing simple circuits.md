---
aliases: ["Thevenin equivalent circuits","I still dislike that name, so he dons't be to be the file name","Thevinins theorem"]
tags: ["Question","QFormat3"]
---

#### What's the method for
## Simplifieing simple circuits
### Method
#### Requirements
- Must be represented in a way that it has 2 terminals
- Must only consist of resistors (that obey [[Ohms law]]), voltage sources and current sources

#### Theory
The method is based on the fact that any "black box" circuit that meets the above requirements can be represented as just a single voltage source and resistor in series:
![[Pasted image 20211114114408.png]]

#### Method
1) Identify the part of the circuit you are going to simplify
2) Find it's resistance between the two terminals by ignoring voltage sources and current sources
3) Find the [[potential difference|voltage]] of the representative voltage source ($V_{TH}$) by finding it's open circuit voltage

### Example
 ![[Pasted image 20211114115018.png]]
 
 1) > First we identify the circuit we want to simplify
 > ![[Pasted image 20211114115154.png]]
> Which is baiscall everything except that resistor

2) > Start by ignoring current sources and voltage sorces 
> ![[Pasted image 20211114115356.png]]
> So: 
> $$\begin{align*}
R=&\dfrac{1}{\dfrac{1}{4+6}+ \dfrac{1}{2}}  \\
=& \frac{5}{3} \Omega
\end{align*}$$
> aw