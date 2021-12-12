---
aliases: ["the 2 entropy equations"]
tags: ["Question","QFormat3"]
---

#### What are and how do you get
## The two [[entropy]] equations
### Final equation
#### [[isobaric expansion or compression|Isobaric]] heating
(extensive form)
> ### $$ S_{12} = mC_V \ln\left(\frac{T_2}{T_1}\right) + mR \ln\left(\frac{V_2}{V_1}\right) $$ 
>> where:
>> $S_{12}=$ [[entropy]] change from $1 \to 2$ 
>> $C_V=$ [[constant volume specific heat]]
>> $R=$ [[individual gas constant|specific gas constant]]
>> $m=$ Mass
>> $T=$ Temperature
>> $V=$ Volume



### Derivation
#### [[isobaric expansion or compression|Isobaric]] heating

So we know that we transfer a small amount of energy ($dQ$) and allow the volume to change ($dV$) which maintains a constant pressure:
(equation: [[isobaric expansion or compression#heat Heat transfer]], [[ideal gas law#Useful Based forms of the equation]])
$$\begin{align*}
dQ = mC_P \cdot dT &= mC_V \cdot dT + P \cdot dV & PV &= mRT \\
&= \frac{mC_V}{T} \cdot dT + \frac{P}{T} \cdot dV & \frac{P}{T} = \frac{mR}{V}\\
&= mC_V \cdot \frac{dT}{T} + mR \cdot \frac{dV}{V}\\
\int^{S_2}_{S_1} 1 \cdot dS &= mC_V \left( \int^{T_2}_{T_1} \frac{1}{T} \cdot dT \right) + mR \left( \int^{V_2}_{V_1} \frac{1}{V} \cdot dV\right) \\
\therefore S_{12} &= mC_V \ln\left(\frac{T_2}{T_1}\right) + mR \ln\left(\frac{V_2}{V_1}\right)
\end{align*}$$

As you can see we now have the [[entropy]] defined interms of two [[state variables]].

#### [[isochoric heat transfer|isochoric]] heating
Here we start with the first equ