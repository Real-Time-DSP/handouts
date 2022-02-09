# LTI filters and frequency selectivity

Linear time-invariant (LTI) systems have many [useful properties](#properties-of-LTI-systems). We can utilize these properties to design [frequency selective](#frequency-selectivity) filters.

## Mathematical definitions

A system is LTI if it satisfies additivity, homogeneity, and time-invariance.

**Additivity**

Let $x_1(t)$ and $x_2(t)$ be arbitrary input signals to a system $\mathcal{S}$. The system satisfies additivity if

$$\mathcal S \left\{x_1(t) + x_2(t)\right\} = \mathcal S \{x_1(t)\} + \mathcal S \{x_2(t) \}$$

**Homogeneity**

Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$. The system satisfies homogeneity if, for any constant $a$,

$$\mathcal S \left\{ax(t)\right\} = a \mathcal S \{ x(t) \}$$

**Time-invariance**

Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$ and let $y(t) = \mathcal S \{ x(t) \}$ be the corresponding output. The system $\mathcal S$ is time-invariant if, for any time shift $\tau$,

$$\mathcal S \left\{x(t-\tau)\right\} = y(t-\tau)$$

A common violation of the time-invariance condition occurs when a system has non-zero initial conditions.

## Properties of LTI systems

An LTI system is [uniquely characterized by its impulse response](#impulse-response-and-convolution). The [Frequency response](#frequency-response) of an LTI system is the Fourier transform of its impulse response.

### Impulse response and convolution

````{panels}
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

### Magnitude and phase response

The frequency response is, in general, complex valued. Typically, we represent it in terms of its magnitude and phase.

````{panels}
:header: text-center
**Continuous time**
^^^
$ \text {Magnitude response} = $

$$| H(j\omega) | = \sqrt { \text{Re} \{ H(j\omega) \} + \text{Im} \{ H(j\omega) \} }$$

$ \text {Phase response} = $

$$ \angle H(j\omega) = \text{atan2} (\text{Im} \{ H(j\omega) \}, \text{Re} \{ H(j\omega) \})$$

---

**Discrete time**
^^^
$ \text {Magnitude response} = $

$$| H(e^{j\omega}) | = \sqrt { \text{Re} \{ H(e^{j\omega}) \} + \text{Im} \{ H(e^{j\omega}) \} }$$

$ \text {Phase response} = $

$$ \angle H(e^{j\omega}) = \text{atan2} (\text{Im} \{ H(e^{j\omega}) \}, \text{Re} \{ H(e^{j\omega}) \})$$

````

where $\text{atan2}$ is the [two argument arctangent](https://en.wikipedia.org/wiki/Atan2).

It is common to use the magnitude/phase representation when measuring and plotting the frequency response of a system.

In MATLAB, the `freqz` function will calculate and plot the magnitude and phase response of a discrete-time LTI system.

## Frequency selectivity

The goal of a filter is to suppress or attenuate some signal components while retaining or boosting others. We often group LTI filters into one of six categories based on their frequency selectivity, i.e. the arrangement of frequency bands that are boosted and frequency bands which are attenuated.

### Lowpass

````{panels}
:header: text-center
**Continuous time averaging filter**
^^^
body

---

**Discrete time averaging filter**
^^^
body

````

### Highpass

````{panels}
:header: text-center
**Continuous time Differentiator**
^^^
body

---

**Discrete time first-order difference**
^^^
body

````

### Bandpass

````{panels}
:header: text-center
**Continuous time elliptic**
^^^
body

---

**Discrete time Parks–McClellan**
^^^
body

````

### Bandstop

````{panels}
:header: text-center
**Continuous time**
^^^
body

---

**Discrete time**
^^^
body

````

### Notch

````{panels}
:header: text-center
**Continuous time**
^^^
body

---

**Discrete time**
^^^
body

````

### All-pass

````{panels}
:header: text-center
**Continuous time**
^^^
body

---

**Discrete time**
^^^
body

````

