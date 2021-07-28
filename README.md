#Neuron Firing
A model neuron based on a basic hypothetical neuron inspired from  this introduction.<Br> 
https://nba.uth.tmc.edu/neuroscience/m/s1/introduction.html

This is largely a simulation of it's behaviour , not a biophysical model .The aim is to use these neurons
to create useful neural networks for exploitation of their capabilities in cognitive tasks , such as driving a 
small RC car.<Br>
<Br>
The "neuron" here certainly does ignore many things of a real world neuron. Real world neurons come in various types and
specialisations , some even with signals sent along their dendrites , some send negative signals as well .
This single 'neuron' here also completely ignores neurotransmitters and their role in transmission.
From what I am aware of , most of what this 'general' neuron is doing ,is concerned with Motor Neurons.

<Br>

The aim is not to create a simulation of a neuron or to study the underlying causes of it's behaviour .This is
only an attempt to 'use' the behaviour of neurons , say , to create a simple network for object analysis.Hence , all
chemical and biological processes in the neuron are being ignored.An attempt has been done to 'imitate'/'emulate'
the biological causes of firing  with simple a very simple analogy dictating their behaviour.
The reason to state this here is that it is quite an important consideration i have made in the entire program , although disconsidering all the internal processing , an attempt has been made to retain the 'qualities' (intensity to frequency relationship,time delay in firing , and action potential threshold) using a
simple mathematical function.<Br>

`y = x -(11- i)`

Where x is an integer denoting time , and i is the Intensity of the stimulus , and y is the resultant Potential of the cell.<Br>
<Br>
The neuron 'Fires' when the Potential crosses the threshold 1, ie , when it reaches an action potential.`
The mathematical function and other process intensive stuff(opening the input.io file repeatedly and checking what's inside) is written in C for no reasons whatsoever.
<Br>
