# Linear time-invariant systems and filters

Adopting a linear time-invariant (LTI) model of a system unlocks several mathematical tools.

* Impulse response and convolution
* Exponentials as eigenfunctions


Often, we will analyze LTI systems that have other important properties.

* Causality
* Stability

Depending on a system's properties and whether it operates in continuous time or discrete time, we often use one or more frequency transforms to analyze LTI systems.

* Fourier transform
* Discrete-time Fourier transform
* Laplace transform
* Z transform

Even if a system does not satisfy the strict mathematical definitions of linearity or time-invariance, we can often approximate the system as LTI and still capture most of the system's behavior.

One of the reasons to study LTI systems is to design and analyze LTI filters. LTI filters are often characterized by their frequency selectivity.

* Lowpass
* Highpass
* Bandpass
* Bandstop and notch
* All-pass

## Mathematical definitions

A system is said to be LTI if it satisfies both the linearity condition and the time-invariance condition.

Using the mathematical definitions is one way to check if a system is LTI. However for systems that are described by a differential equation, difference equation or by their impulse response, there are other ways to check if the system is LTI.

### Linearity

A system is linear if it satisfies additivity and homogeneity.

#### Additivity

#### Homogeneity

### Time-invariance

Let $x(t)$ be an arbitrary input to a system $\mathscr{S}$ and let $y(t)$ be the corresponding output, i.e., $\mathscr S \left\{x(t)\right\} = y(t)$.

If $\mathscr S \left\{x(t-\tau)\right\} = y(t-\tau)$ for every possible time shift $\tau$, then the system $\mathscr S$ is time-invariant.

A common violation of the time-invariance condition occurs when a system has non-zero initial conditions.

## Properties of LTI systems

### Impulse response and convolution

### Exponentials as eigenfunctions

## Related properties

### Causality

### Stability

## Frequency analysis

### Fourier transform

### Discrete-time Fourier transform

### Laplace transform

### Z transform

## Frequency selectivity

* Lowpass
* Highpass
* Bandpass
* Bandstop and notch
* All-pass
