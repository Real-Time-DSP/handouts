# LTI filters and frequency selectivity

Linear time-invariant (LTI) systems have many [useful properties](#properties-of-LTI-systems). We can utilize these properties to design [frequency selective](#frequency-selectivity) filters.

## Mathematical definitions

::: {panels}
:container: container-lg pb-4
:header: text-center

**Additivity**
^^^
Let $x_1(t)$ and $x_2(t)$ be arbitrary input signals to a system $\mathcal{S}$. The system satisfies additivity if

$$\mathcal S \left\{x_1(t) + x_2(t)\right\} = \mathcal S \{x_1(t)\} + \mathcal S \{x_2(t) \}$$

---

**Homogeneity**
^^^

Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$. The system satisfies homogeneity if, for any constant $a$,

$$\mathcal S \left\{ax(t)\right\} = a \mathcal S \{ x(t) \}$$

---

**Time-invariance**
^^^
Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$ and let $y(t) = \mathcal S \{ x(t) \}$ be the corresponding output. The system $\mathcal S$ is time-invariant if, for any time shift $\tau$,

$$\mathcal S \left\{x(t-\tau)\right\} = y(t-\tau)$$

---

**Linear time-invariant (LTI)**
^^^
A system is linear time-invariant (LTI) if it satisfies the additivity, homogeneity, and time-invariance properties. A common way for a system to fail to violate these properties is if the system has has nonzero initial conditions.
:::

## Properties of LTI systems

An LTI system is [uniquely characterized by its impulse response](#impulse-response-and-convolution). The [Frequency response](#frequency-response) of an LTI system is the Fourier transform of its impulse response.

### Impulse response and convolution

````{panels}
:container: container-lg pb-3
:header: text-center

**Continuous time**
^^^
A continuous time impulse, (also known as the Dirac delta) can be defined as a unit area pulse in the limit that it's duration approaches zero.

$$\delta(t) = \lim_{\epsilon \to 0}{\frac{\text{rect}(t/\epsilon)}{\epsilon}}$$

If a system is LTI, then its impulse response $h(t) = \mathcal S \{ \delta(t) \}$ uniquely characterizes the system. The output $y(t)$ of an LTI system is the convolution between the input $x(t)$ and the system's impulse response $h(t)$.

$$ y(t) = x(t) * h(t) = \int_{-\infty}^{\infty}{x(t-\tau)h(\tau) d \tau}$$

---
**Discrete time**
^^^
A discrete time impulse, (also known as the Kronecker delta) can be defined as a piecewise function.

$$\delta[n] = \left\{ \begin{array}{ll} 1 & \quad n = 0 \\ 0 & \quad n \neq 0 \end{array} \right.$$

If a system is LTI, then its impulse response $h[n] = \mathcal S \{ \delta[n] \}$ uniquely characterizes the system. The output $y[n]$ of an LTI system is the convolution between the input $x[n]$ and the system's impulse response $h[n]$.

$$ y[n] = x[n] * h[n] = \sum_{-\infty}^{\infty}{x[n-m]h[m]}$$

````

### Frequency response

Complex exponentials are eigenfunctions of LTI systems. Combined with the previous property, This allows us to uniquely characterize a system by its frequency response.

```{admonition} Eigenfunctions
If application of the system $\mathcal S$ to the signal $x(t)$ results in scaling only ( i.e. $\mathcal S \{x(t)\} = \lambda x(t) $ for some constant $\lambda$ ) then we say that $x(t)$ is an eigenfunction of the system and $\lambda$ is the corresponding eigenvalue.
```

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time**
^^^
If the input to an LTI system is a complex exponential $x(t) = e^{j \omega t}$, then the corresponding output is

$$ y(t) = H(j \omega) e^{j\omega t} $$

where $H(j\omega)$ (called the frequency response) is the Fourier transform of the impulse response or, equivalently, the Laplace transform of the impulse response evaluated as $s=j\omega$.

$$H(j\omega) = \mathcal F \{ h(t) \} = \left. \mathcal L \{ h(t) \} \right| _{s=j\omega}$$

---

**Discrete time**
^^^
If the input to an LTI system is a complex exponential $x[n] = e^{j \omega n}$, then the corresponding output is

$$ y[n] = H(e^{j\omega}) e^{j\omega n} $$

where $H(e^{j\omega})$ (called the frequency response) is the Discrete-time Fourier transform of the impulse response or, equivalently, the Z transform of the impulse response evaluated at $z = e^{j\omega}$.

$$H(e^{j\omega}) = \text{DTFT} \{ h[n] \} = \left. \mathcal Z \{ h[n] \} \right| _{z=e^{j\omega}}$$

````

We often write $H(\omega)$ instead of $H(j\omega)$ or $H(e^{j\omega})$.

### Magnitude and phase response

The frequency response is, in general, complex valued. Typically, we represent it in terms of its magnitude and phase.

$$ \text {Magnitude response} = | H(\omega) | = \sqrt { \text{Re} \{ H(\omega) \} + \text{Im} \{ H(\omega) \} }$$

$$ \text {Phase response} = \angle H(\omega) = \text{atan2} (\text{Im} \{ H(\omega) \}, \text{Re} \{ H(\omega) \})$$

where $\text{atan2}$ is the [two argument arctangent](https://en.wikipedia.org/wiki/Atan2).

It is common to use the magnitude/phase representation when measuring and plotting the frequency response of a system. Typically, the magnitude response is expressed in decibels

$$\text{Magnitude response in decibels} = 10 \log_{10}{|H(\omega)|^2} = 20 \log_{10}{|H(\omega)|}$$

In MATLAB, the `freqz` function will calculate and plot the magnitude and phase response of a discrete-time LTI system.

## Frequency selectivity

The goal of a filter is to suppress or attenuate some signal components while retaining or boosting others. We often group LTI filters into six categories based on their frequency selectivity, i.e. the arrangement of frequency bands that are boosted relative to the bands which are attenuated.

* [Lowpass](#lowpass)
* [Highpass](#highpass)
* [Bandpass](#bandpass)
* [Bandstop](#bandstop)
* [Notch](#notch)
* [Allpass](#allpass)


### Lowpass

![](img/lowpass.svg)

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example: averaging filter**
^^^
body

---

**Discrete time example: averaging filter**
^^^
body

````

### Highpass

![](img/highpass.svg)

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example: differentiator**
^^^
body

---

**Discrete time example: first-order difference**
^^^
body

````

### Bandpass

![](img/bandpass.svg)

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example**
^^^
body

---

**Discrete time example**
^^^
body

````

### Bandstop

![](img/bandstop.svg)

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example**
^^^
body

---

**Discrete time example**
^^^
body

````

### Notch

![](img/notch.svg)

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example**
^^^
body

---

**Discrete time example**
^^^
body

````

### Allpass

Allpass filters have a flat magnitude response but affect the signal's phase. Two common examples are the [Hilbert transform](https://en.wikipedia.org/wiki/Hilbert_transform) and the ideal delay.

When an [equalizer](https://en.wikipedia.org/wiki/Equalization_(communications)) is applied to correct for distortion, the cascade of the original system and the equalizer may be modeled as an all-pass filter.

````{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time example: Hilbert transform**
^^^
body

---

**Discrete time example: Delay**
^^^
body

````
