---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Mohrs circle
### Useful stuff
This is a useful techinque for presenting all the possible shear and normal stresses acting on some [[stress transformation for plane stress|trasformed stress]]. Basically this is the way to comprehend the stresses acting in all directions in a intuitive way. (not using that as a buzzword, I mean it, [[step 1|you'll see]]. This is [[based redpilled ect|acc quite neat]] tbh. ([[next part lol]]) )

The following is an equation defining the relationship between the normal and shear stress for any stress transformation:

> ### $$ \left(\sigma_{x`x`} - \frac{\sigma_{xx} + \sigma_{yy}}{2}\right)^{2} + \sigma_{x`y`}^{2} = \left(\frac{\sigma_{xx}-\sigma_{yy}}{2}\right)^{2} + \sigma_{xy}^{2} $$ 
> ### $$ \left(\sigma_{x`x`} - \sigma_{average} \right)^{2} + \sigma_{x`y`}^{2} = R $$ 
>> where:
>> $R=\sqrt{\left(\frac{\sigma_{xx}-\sigma_{yy}}{2}\right)^{2} + \sigma_{xy}^{2}}$ 
>> $\sigma_{average}= \frac{\sigma_{xx} + \sigma_{yy}}{2}$
>> $\sigma_{x`x`}=$ Normal stress at some transformed state
>> $\sigma_{x`y`}=$ Shear stress at some transformed state
>> $\sigma_{xx}=$ Refrence normal stress (xx)
>> $\sigma_{yy}=$ Refrence normal stress (yy)
>> $\sigma_{xy}=$ Refrence shear stress

Which when plotted resaults in the following:
![[Pasted image 20220301222636.png]]

### Proof and theory
Basically to get the equation above what you need to do is use:
![[stress transformation for plane stress#^52d731]]
![[stress transformation for plane stress#^b65568]]
By equating these two using $\theta$ we can use math wizardry to get it into the form above:
$$\begin{align*}
\sigma_{x'x'} &= \sigma_{yy} \sin^{2}\theta + \sigma_{xx} \cos^{2}\theta + \sigma_{xy} \sin2\theta & \sigma_{x'y'} &= (\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}(\cos^{2}\theta- \sin^{2}\theta )\\
\sigma_{x'x'} &= \sigma_{yy} \frac{1-\cos 2\theta}{2} + \sigma_{xx} \frac{1+\cos 2\theta}{2} + \sigma_{xy} \sin2\theta & \sigma_{x'y'} &= (\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}(\frac{1+\cos 2\theta}{2}- \frac{1-\cos 2\theta}{2} )\\
\sigma_{x'x'} &=  \frac{\sigma_{yy}-\sigma_{yy}\cos 2\theta}{2} + \frac{\sigma_{xx}+\sigma_{xx}\cos 2\theta}{2} + \sigma_{xy} \sin2\theta & 
\sigma_{x'y'} &= (\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}(\frac{\cos 2\theta}{2}+ \frac{\cos 2\theta}{2} )\\
\sigma_{x'x'} &=  \frac{\sigma_{xx}+\sigma_{yy}}{2} + \frac{\sigma_{xx} - \sigma_{yy}}{2}\cos 2\theta + \sigma_{xy} \sin2\theta & 
\sigma_{x'y'} &= (\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}\cos 2\theta \\
\sigma_{x'x'} - \frac{\sigma_{xx}+\sigma_{yy}}{2} &=  \frac{\sigma_{xx} - \sigma_{yy}}{2}\cos 2\theta + \sigma_{xy} \sin2\theta \\
\left(\sigma_{x'x'} - \frac{\sigma_{xx}+\sigma_{yy}}{2} \right)^{2}&=  \left(\frac{\sigma_{xx} - \sigma_{yy}}{2}\cos 2\theta + \sigma_{xy} \sin2\theta\right)^{2} & 
\sigma_{x'y'}^{2} &= \left((\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}\cos 2\theta\right)^{2} \\
\end{align*}$$

Then we just add them together: