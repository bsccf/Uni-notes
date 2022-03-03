---
aliases: ["EBE","extended bernouli equation"]
tags: ["Question","QFormat3"]
---

#### What is the
## Steady mechanical energy equation
### The equation
Basically this is the same as the [[steady flow energy equation]] but it has some extra terms slapped on to account for mechanical losses.

> ### $$ - \frac{\dot{W}}{m} = \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{out} - \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{in} + f \frac{L}{2d} \bar{U}^{2} + \sum\limits_{n} k_{n} \left(\frac{1}{2} \bar{U}^{2}\right) $$
>> where:
>> $W=$ work done, ’non-fluid’ energy transfer. For example electrical work increasing the fluid pressure in a pump. (positive is work out, negative is work in)
>>  $p=$ pressure
>>  $\rho=$ fluid density
>>  $g=$ acceleration due to gravity
>>  $z=$ height of centre of cross sectional area
>>  $\alpha=$ [[kinetic energy correction factor]]
>>  $d=$ pipe diameter
>>  $L=$ pipe length
>>  $f=$ emperical coefficient relating to friction
>>  $k_{n}=$ the coefficient relating to that specific energy loss
>>  $\bar{U}=$ velocity ([[UNFINISHED STUFF|not 100% sure if it dosn't have extra special meaning]])

This equation only assumes [[steady flow]] and there are 2 ports, so it is widely applicable.

### Equation parts
The equation has lots of bits each with it's own meaning, so I'll break it down to be more understandable.

#### Energy stored in the fluid

$$ \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{out} - \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{in} $$
Represents the change in energy stored in the fluid (excluding heat), so pressure, kinetic and gpe are represented here.

#### Frictional losses
$$ f \frac{L}{2d} \bar{U}^{2} $$

This uses a coefficient that is specific to the pipe $f$ to adjust for losses due to friction in the strait sections of pipe