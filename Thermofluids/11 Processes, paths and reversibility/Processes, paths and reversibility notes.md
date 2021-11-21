---
aliases: [""]
tags: ["NotesPage"]
---

# Processes, paths and reversibility notes

# Ok I will come back to this later, this feels like something I will make better notes on later

#### Intro and contents
- [[process (thermofluids)]]
- [[cycle (themofluids)]]
- [[reversibility (thermofluids)]]

## Expanded articles
![[process (thermofluids)]]


### Pasted stuff

Purpose of this lecture 
Define paths, cycles and reversibility
Investigate named processes in some detail

 Terminology: Initial/final states: Process, Path and Cycle

Trying to describe change quantitatively
state: A gas in equilibrium.
process: doing something to a gas to change its state.
initial/final: (states) of a process
path: The trajectory in state-space by the process.
Points to note:
A 2D plot fully describes the process, because of the two-property rule.
To specify the process (and define the path) the initial and final states and the
transfers across the system boundary must be defined 
Unless we make a further assumption, we generally do not know the state of the system in between the initial and final states.
If we move from state 1 along path A to state 2 Then From state 2 along path B back to state 1
Then we have performed a ……………….
i.e. ended up where we started via a series of processes (more than 1, usually 4 for a heat engine/pump)


Reversible and Irreversible Processes
A reversible process will be able to....
Reverse its trajectory along a path
characteristics of reversible processes
heat transfer: no temperature difference, slow, large areas
 motion (work): zero friction
types of reversible processes
internally reversible: system change is reversible
externally reversible: environment does not change
fully reversible: internal + external
Example
An irreversible quasi-equilibrium work process is the slow compression of a gas in an insulated piston-cylinder with friction present.
A fully reversible quasi-equilibrium heat transfer process is the very slow expansion of very large and thin walled frictionless piston-cylinder at constant temperature.
An internally reversible quasi-equilibrium heat transfer process is the constant volume heating of a cold gas.
This is directly related to entropy generation, which leads to engine efficiency considerations.
Recall that: 
Entropy is a measure of disorder of a system
Entropy increases with temperature
Now know that:
Increasing Entropy means more “lost” useful energy.







 Process Types (1/4): Isochoric (Constant Volume) heat transfer
Used for: efficient heat addition to increase temperature such as fast Combustion Petrol Engines
Typically, the gas is heated, increasing the pressure, in a rigid container, Process 3 to 1 on the PV graph. Heat rejection/removal is process path 1 to 3. 
Initial, final states are related by:
Conservation of Energy: Q13 – W13 = Eu,13  or  q13 - w13 = eu,13
 Work transfer:   W13 = 0
Heat Transfer: Q13 =  W13 +  Eu,13 = mCV(T3-T1)
Or….. q13 = w13 + eu,13 = CV(T3-T1)
Q13 = Eu,13 (heat transfer is the internal energy change)
Reversibility – The heat transfer occurs over the temperature range 
Process Types (2/4): Isobaric (Constant Pressure) Expansion/Compression 
Used for: Slow/steady combustion: boilers, gas turbines
Energy (heat) transfer) raises the internal energy and does displacement work. The temperature rises to maintain the pressure as volume increases.
Process 1 to 2 on the PV graph
Initial, final states are related by:  
Conservation of Energy: Q12 – W12 = Eu,12  or  q12 - w12 = eu,12
 Work transfer:   W12 = ʃ pdV = p(V2-V1) or w12 = ʃ pdV = p(v2-v1)
Heat Transfer: Q12 =  W12 +  Eu,12 = mCp(Thigh-T1) = p(V2-V1) + mCV(Thigh-T1)
Or….. q12 = w12 + eu,12 = Cp(Thigh-T1) = p(v2-v1) + CV(Thigh-T1)
Q12 = Eh,12 = Eu,12 + pΔV (heat transfer is the enthalpy change)
Reversibility – The heat transfer occurs over the temperature range
A problem: 
And the method we always use to solve them… so write it down (hint) 
Q. A gas-based thermometer is placed in a water bath at 0°C and has a volume of 100cm3. It is transferred to boiling liquid chlorine and contracts to 87.2cm3 for the same internal pressure. At what temperature does chlorine boil?
















Process Types (3/4): Isothermal (Const. Temperature) Expansion/Compression 
Used for: Impractically slow expansion, theoretical engine efficiency benchmarking 
Heat transfer must occur over a negligible temperature difference – large areas.)
 Process 1 to 4 on the PV graph
Initial, final states are related by: 

 Conservation of Energy: Q14 – W14 = Eu,14  or  q14 - w14 = eu,14
Work transfer:

Heat Transfer: Q14 =  W14  Note that   Eu,14 = mCV(T1-T1) = 0
Or….. q14 = w14  Heat transfer is the work done
Reversibility – All heat transfer occurs at the isotherm temperature.

Process Types (4/4): Adiabatic (Zero heat transfer) Expansion/Compression 
Used for: occurs in a thermally insulated container. A good approximation for the power and compression strokes in internal combustion engines. Work processes in the Carnot cycle. 
pVγ = constant
 Process 1 to 5 on the PV graph
Initial, final states are related by:

 Conservation of Energy: Q15 – W15 = Eu,15  or  q15 - w15 = eu,15
Work transfer:

Heat Transfer: Q15 = 0 Note that   Eu,15 = mCV(T2-T1) 
Conservation of Energy: – W15 = Eu,15  = mCV(T2-T1) 
Reversibility – Zero heat transfer, the process is reversible if frictionless
We have investigated 2 processes that could be reversible:
…………
…………
Both play a part in the Carnot cycle (lecture 2 and the next lecture)
What is the Carnot cycle? What did he propose? 
So we know that entropy is minimised with Carnot and that it is some measure of disorder of a system (last lecture) and thus the loss of useful mechanical work
Examples of Irreversibility and Entropy Generation
A good engineer is an entropy minimiser
Understanding of the fundamental physics and the design of technology that minimises irreversible entropy generation!
Examples of irreversible entropy generation in Thermofluids
viscous friction (Shear Stresses) in fluid flow - leads to pressure drops in pipes, drag on objects.
Turbulent flow - much larger pressure drops in pipes, drag on objects.
Heat transfer across a temperature difference.
Unrestrained expansion.
Shock waves in compressible fluids (not covered here).
Mixing of different fluids (not covered here).
Phase change (not covered here).
---------------------
Entropy is essentially a measure of disorder of a system.
What might we need to have an isentropic process? 
No increase in disorder so… 
Therefore, any reversible ………………. process is also …………………. 

Today’s Learning outcomes
⦁	Knowledge of the work and heat transfers of 4 named processes: Isochoric, Isobaric, Isothermal, and adiabatic
⦁	Applied our knowledge to solve a problem involving an isobaric process and Knowledge that the methodology used can be applied to most problems
⦁	Understanding reversibility and a little more about Entropy
