# A 'generalised' 'neuron' (Not really , but can call it as something inspired by the neuron) with one axon and
# several dendrites.

# Make sure that intensity of given stimulus is a integer between 0 to 10 only
import os


class neuron:
    def __init__(self):
        self.stimulus_cache = 0

    def action(self):
        with open("input.io", 'w') as input_output:
            print(self.stimulus_cache)
            input_output.write(f"{self.stimulus_cache}")  # This will change the rate of firing of the neuron.


class Dendrite:
    def __init__(self, parent):
        self.parent = parent
        self.stimulation = 0

    def stimulate(self, intensity):
        if self.stimulation != 0:
            # Stimulation will work only after the previous stimulation is stopped.
            self.stop()

        # intensity here refers to a measure of intensity , that is , the magnitude of stimulation . The number of
        # signals fired is directly proportional to the intensity.
        self.parent.stimulus_cache += intensity
        self.parent.action()
        self.stimulation = intensity

    def stop(self):
        self.parent.stimulus_cache -= self.stimulation
        self.parent.action()
        self.stimulation = 0


# Making a neuron

Neuron = neuron()
dendrite1 = Dendrite(Neuron)
dendrite2 = Dendrite(Neuron)

# Staring its
os.startfile("output.exe")

dendrite1.stimulate(1)

# Open in command line and put dendrite1.stimulate(1) to stimulate , observe the output.exe that shows the firing of
# the neuron. Use dendrite1.stop() to stop firing caused due to entire1 , this doesnt affect firing caused due to
# other dendrites being stimulated . Note that stimulation at all the dendrites add up and the whole is responsible
# for the firing . To stop firing , all dendrite stimulation should be stopped.

# For an analogy hyperpolarisation effect , one can try putting in negative numbers , which negatively affects the
# function inside , showing something similar to hyperpolarisation , ie , depolarisation in the opposite direction.
