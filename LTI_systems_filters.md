# LTI filters and frequency selectivity

Adopting a linear time-invariant (LTI) model of a system can simplify analysis for three (related) reasons

1. [An LTI system is uniquely characterized by its impulse response](#impulse-response-and-convolution)
2. [Complex exponentials (including sinusoids) are eigenfunctions of LTI systems
3. [The Fourier transform of the impulse response is the frequency response](#frequency-analysis)

We can utilize these properties to design LTI filters based on a desired [frequency selectivity](#frequency-selectivity).

* [Lowpass](#lowpass)
* [Highpass](#highpass)
* [Bandpass](#bandpass)
* [Bandstop](#bandstop)
* [Notch](#notch)
* [All-pass](#all-pass)

Even if a system does not satisfy the strict mathematical definitions of linearity or time-invariance, we can often approximate the system as LTI and still capture much of the system's behavior.

For a filter be be realizable and operate in real-time, it must be [causal](#causality). Typical frequency selective filters are [stable systems](#stability). However, unstable LTI systems can also be useful (e.g. oscillators).

## Mathematical definitions

A system is said to be LTI if it satisfies both the linearity condition and the time-invariance condition.

Using the mathematical definitions is one way to check if a system is LTI. However for systems that are described by a differential equation, difference equation or by their impulse response, there are other ways to check if the system is LTI.

### Linearity

A system is linear if it satisfies additivity and homogeneity.

**Additivity**

Let $x_1(t)$ and $x_2(t)$ be an arbitrary input signals to a system $\mathcal{T}$ and let $y_1(t)$ and $y_2(t)$ be the corresponding outputs.

The system $\mathcal T$ satisfies additivity if

$$\mathcal T \left\{x_1(t) + x_2(t)\right\} = y_1(t)+y_2(t)$$

**Homogeneity**

Let $x(t)$ be an arbitrary input to a system $\mathcal{T}$ and let $y(t)$ be the corresponding output.

The system $\mathcal T$ satisfies homogeneity if, for any constant $a$,

$$\mathcal T \left\{ax(t)\right\} = ay(t)$$

### Time-invariance

Let $x(t)$ be an arbitrary input to a system $\mathcal{T}$ and let $y(t)$ be the corresponding output.

The system $\mathcal T$ is time-invariant if, for any time shift $\tau$,

$$\mathcal T \left\{x(t-\tau)\right\} = y(t-\tau)$$

A common violation of the time-invariance condition occurs when a system has non-zero initial conditions.

## Properties of LTI systems

If a system is LTI, then it can be uniquely described by its impulse response. The

### Impulse response and convolution

| Continuous Time | Discrete Time |
| :-------------: | :-----------: |
| test            | test          |

### Exponentials as eigenfunctions

## Related system properties

### Causality

### Stability

## Frequency analysis

Depending on a system's properties and whether it operates in continuous time or discrete time, we often use one or more frequency transforms to analyze LTI systems.

* Fourier transform
* Discrete-time Fourier transform
* Laplace transform
* Z transform

### Fourier transform

### Discrete-time Fourier transform

### Laplace transform

### Z transform

## Frequency selectivity

### Lowpass
### Highpass
### Bandpass
### Bandstop
### Notch
### All-pass
