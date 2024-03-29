<style>
@media print {
    .pagebreak { page-break-before: always; } /* page-break-after works, as well */
}
</style>

# LTI filters and frequency selectivity

Linear time-invariant (LTI) systems have many [useful properties](#properties-of-lti-systems). We can utilize these properties to design [frequency selective](#frequency-selectivity) filters.

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

### Properties of LTI systems

An LTI system is [uniquely characterized by its impulse response](#impulse-response-and-convolution). The [Frequency response](#frequency-response) of an LTI system is the Fourier transform of its impulse response.

### Impulse response and convolution

:::{panels}
:container: container-lg pb-3
:header: text-center

**Continuous time**
^^^
A continuous time impulse, (also known as the Dirac delta) can be defined as a unit area pulse in the limit that its duration approaches zero.

$$\delta(t) = \lim_{\epsilon \to 0}{\frac{\text{rect}(t/\epsilon)}{\epsilon}}$$

If a system is LTI, then its impulse response $h(t) = \mathcal S \{ \delta(t) \}$ uniquely characterizes the system. The output $y(t)$ of an LTI system is the convolution between the input $x(t)$ and the system's impulse response $h(t)$.

$$ y(t) = x(t) * h(t) = \int_{\tau = -\infty}^{\infty}{x(t-\tau)h(\tau) d \tau}$$

---
**Discrete time**
^^^
A discrete time impulse, (also known as the Kronecker delta) can be defined as a piecewise function.

$$\delta[n] = \left\{ \begin{array}{ll} 1 & \quad n = 0 \\ 0 & \quad n \neq 0 \end{array} \right.$$

If a system is LTI, then its impulse response $h[n] = \mathcal S \{ \delta[n] \}$ uniquely characterizes the system. The output $y[n]$ of an LTI system is the convolution between the input $x[n]$ and the system's impulse response $h[n]$.

$$ y[n] = x[n] * h[n] = \sum_{m=-\infty}^{\infty}{x[n-m]h[m]}$$

:::

### Frequency response

Complex exponentials are eigenfunctions of LTI systems. Combined with the previous property, This allows us to uniquely characterize a system by its frequency response.

```{admonition} Eigenfunctions
If application of the system $\mathcal S$ to the signal $x(t)$ results in scaling only ( i.e. $\mathcal S \{x(t)\} = \lambda x(t) $ for some constant $\lambda$ ) then we say that $x(t)$ is an eigenfunction of the system and $\lambda$ is the corresponding eigenvalue.
```

:::{panels}
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

:::

We often write $H(\omega)$ instead of $H(j\omega)$ or $H(e^{j\omega})$.

### Magnitude and phase response

The frequency response is, in general, complex valued. Typically, we represent it in terms of its magnitude and phase.

$$ \text {Magnitude response} = | H(\omega) | = \sqrt { \text{Re} \{ H(\omega) \}^2 + \text{Im} \{ H(\omega) \}^2 }$$

$$ \text {Phase response} = \angle H(\omega) = \text{atan2} (\text{Im} \{ H(\omega) \}, \text{Re} \{ H(\omega) \})$$

where $\text{atan2}$ is the [two argument arctangent](https://en.wikipedia.org/wiki/Atan2).

It is common to use the magnitude/phase representation when measuring and plotting the frequency response of a system. Typically, the magnitude response is expressed in decibels

$$\text{Magnitude response in decibels} = 10 \log_{10}{|H(\omega)|^2} = 20 \log_{10}{|H(\omega)|}$$

In MATLAB, the `freqz` function will calculate and plot the magnitude and phase response of a discrete-time LTI system. The freqz function computes the the z-transform and replaces $z=e^{j\omega}$ to convert to the frequency domain, which might not always be valid.

<div class="pagebreak"> </div>

## Frequency selectivity

The goal of a filter is to suppress or attenuate some signal components while retaining or boosting others. We often group LTI filters into six categories based on their frequency selectivity, i.e. the arrangement of frequency bands that are boosted relative to the bands which are attenuated.

:::{panels}
:container: container-lg pb-3
:header: text-center
**[Lowpass](#lowpass)**
^^^
![](img/lowpass.svg)
---
**[Highpass](#highpass)**
^^^
![](img/highpass.svg)
---
**[Bandpass](#bandpass)**
^^^
![](img/bandpass.svg)
---
**[Bandstop](#bandstop-and-notch)**
^^^
![](img/bandstop.svg)
---
**[Notch](#bandstop-and-notch)**
^^^
![](img/notch.svg)
---
**[Allpass](#allpass)**
^^^
![](img/allpass.svg)
:::

<div class="pagebreak"> </div>

### Lowpass

![](img/lowpass.svg)

:::{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time lowpass example**
^^^
Impulse response:

$$h(t) = e^{-t} u(t)$$

Frequency response:

$$H(f) = \frac{1}{1 + j2\pi f}$$

![](img/ct_lowpass.svg)

---

**Discrete time moving average**
^^^
Impulse response:

$$h[n] = \frac{1}{5} \left( \delta[n] + \delta[n-1] + \cdots \delta[n-4] \right)$$

Frequency response:

$$H(\omega) = e^{-2j \omega} \frac{\sin{(5\omega /2)}}{5 \sin{(\omega/2)}}$$

![](img/dt_lowpass.svg)

:::

<div class="pagebreak"> </div>

### Highpass

![](img/highpass.svg)

:::{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time highpass example**
^^^
Impulse response:

$$h(t) = \delta(t) - e^{-t} u(t)$$

Frequency response:

$$H(f) = \frac{j 2\pi f}{1+ j2\pi f}$$

![](img/ct_highpass.svg)

---

**Discrete time first order difference**
^^^
Impulse response:

$$h[n] = \frac{1}{2} \left( \delta[n] - \delta[n-1] \right)$$

Frequency response:

$$H(\omega) = \frac{1}{2} \left( 1 - e^{-j\omega} \right)$$

![](img/dt_highpass.svg)

:::

<div class="pagebreak"> </div>

### Bandpass

![](img/bandpass.svg)

:::{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time bandpass example**
^^^
Impulse response:

$$h(t) = e^{-t} \cos{(2\pi t)} u(t)$$

Frequency response:

$$H(f) = \frac{j 2 \pi f}{(2\pi)^2 + (j2 \pi f)^2}$$

![](img/ct_bandpass.svg)

---

**Discrete time bandpass example**
^^^
Impulse response:

$$h[n] = e^{-n/4} \cos{\left( \frac{\pi}{2} n \right)} u[n]$$

Frequency response:

$$H(\omega) = \frac{1}{1+e^{-(2j\omega + ¼)}}$$

![](img/dt_bandpass.svg)

:::

<div class="pagebreak"> </div>

### Bandstop and notch

![](img/bandstop.svg)

:::{panels}
:container: container-lg pb-3
:header: text-center
**Continuous time bandstop example**
^^^
Impulse response:

$$h(t) = \delta(t) - 2e^{-t} (1-t) u(t)$$

Frequency response:

$$H(f) = \frac{(2\pi j f)^2 + 1}{(2\pi j f + 1)^2}$$

![](img/ct_bandstop.svg)

---

**Discrete time notch example**
^^^
Impulse response:

$$h[n] = 2\delta[n] - 2^{-n/2} \cos{\left( \frac{\pi}{2} n \right)} u[n]$$

Frequency response:

$$H(\omega) = \frac{1 + e^{-2j\omega}}{1 + \frac{1}{2}e^{-2j\omega}}$$

![](img/dt_notch.svg)

:::

### Allpass

Allpass filters have a flat magnitude response but affect the signal's phase. Two common examples are the ideal delay and the [Hilbert transform](https://en.wikipedia.org/wiki/Hilbert_transform).