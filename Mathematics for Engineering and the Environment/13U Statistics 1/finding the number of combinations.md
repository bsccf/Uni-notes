---
aliases: ["combination","permutation"]
tags: ["Question","QFormat3"]
---

#### Describe methods for
## Finding the number of combinations
### [[mutually exclusive events|Mutually exclusive]] sequence of events
#### Theory
For many situations you have a discrete variable that can take on some number of states and then a squence of these variables, for some set length of sequence there is a set number of combinations possible, for example if a 6 sided dice is rolled twice the number of possible outcomes is $6^{2}=36$ so expressed mathamatically:

> ### $$ N = P^{L} $$ 
>> where:
>> $N=$ number of possible outcomes
>> $P=$ number of possible [[mutually exclusive events]] per outcome
>> $L=$ length of outcome list

#### Example
> Find the number of possible combinations of some hypothetical 3 sided coin with states {H,T,A} thrown 2 times
 
$3^{2} = 9$
9 times.

(HH, HT, HA, TH, TT, TA, AH, AT, AA)

### [[mutually exclusive events|Mutually exclusive]] tally of events (combination)
#### Theory
So basically take [[finding the number of combinations#mutually exclusive events Mutually exclusive sequence of events|the thing above]] but just tally how much each event occurs, like flipping a coin 100 times and seeing the total head and total tail occurances. Instead you would get this equation:

> ### $$ N =  $$ 
>> where:
>> $N=$ number of possible outcomes
>> $P=$ number of possible [[mutually exclusive events]] per outcome
>> $L=$ length of outcome list