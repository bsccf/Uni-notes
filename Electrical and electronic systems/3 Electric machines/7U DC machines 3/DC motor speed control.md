---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we achieve
## DC motor speed control
The simplest solution is slapping a DC motor in series with a [[rheostat]], but this kinda sucks because now you loose power as heat for no good reason, hence it is a trash approach and anyone who suggests it should/will/is getting executed by firing squad.

Now the galaxy brain approach (which I 100% didn't just learn about, and knew all along (since birth actually) because I would never consider the previous approach) is to slap a transistor in there, then use a really fast [[alternating current]] with the following waveform and circuit configuration:
![[Pasted image 20220224142943.png]]
By also slapping an [[inductor]] in series with the motor you can ensure a more stable current, and given a really high frequency the current will basically approximate as constant.

The mean current can be found using:
> ### $$ I_{mean} = \frac{t_{on}}{t_{on}+} $$ 
>> where:
>> $=$ 
>> $=$
>> $=$