---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are the
## Elementary row operations with constant solutions
When you have a matrix (any dimentions that are valid for [[solving linear equations with matricies]]) like the following:
$$\begin{align*}
\begin{pmatrix} a & b & c \\ d & e & f \\ g  & h & i \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} &= \begin{pmatrix}  A \\ B \\ C\end{pmatrix} 
\end{align*}$$
Then there are certain row operations that can be used to manipulate the matrix without changing the values of $x,y,z$.

These are [[elementary row operations with constant solutions]]:
1) Multiplication of a row by a constant
2) Interchange of two rows
3) Addition or subtraction of two rows

#### Multiplication of a row by a constant
> ### $$ \begin{pmatrix} a & b & c \\ d & e & f \\ g  & h & i \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}  A \\ B \\ C\end{pmatrix}  \rightarrow \begin{pmatrix} \lambda a & \lambda b & \lambda c \\ d & e & f \\ g  & h & i \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}  \lambda A \\ B \\ C\end{pmatrix} $$ 
>> Properties:
>> - The solutions for $x,y,z$ remain constant
>> - This multiplication can be applied to any row
>> 
>> where:
>> $\lambda \neq 0$

#### Interchange of two rows
> ### $$ \begin{pmatrix} a & b & c \\ d & e & f \\ g  & h & i \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}  A \\ B \\ C\end{pmatrix}  \rightarrow \begin{pmatrix} b & a & c \\ e & d & f \\ h  & g & i \end{pmatrix} \begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}  B \\ A \\ C\end{pmatrix} $$ 
>> Properties:
>> - The solutions for $x,y,z$ remain constant
>> - This multiplication can be applied to any row
>> 
>> where:
>> $\lambda \neq 0$