# LTI filters and frequency selectivity

Linear time-invariant (LTI) systems have many [useful properties](#properties-of-LTI-systems). We can utilize these properties to design [frequency selective](#frequency-selectivity) filters. For a filter be be realizable and operate in real-time, it must be [causal](#causality). Typical frequency selective filters are [stable systems](#stability). However, unstable LTI systems can also be useful (e.g. oscillators).

## Mathematical definitions

A system is LTI if it satisfies additivity, homogeneity, and time-invariance.

**Additivity**

Let $x_1(t)$ and $x_2(t)$ be an arbitrary input signals to a system $\mathcal{S}$ and let $y_1(t)$ and $y_2(t)$ be the corresponding outputs. The system $\mathcal S$ satisfies additivity if

$$\mathcal S \left\{x_1(t) + x_2(t)\right\} = y_1(t)+y_2(t)$$

**Homogeneity**

Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$ and let $y(t)$ be the corresponding output. The system $\mathcal S$ satisfies homogeneity if, for any constant $a$,

$$\mathcal S \left\{ax(t)\right\} = ay(t)$$

**Time-invariance**

Let $x(t)$ be an arbitrary input to a system $\mathcal{S}$ and let $y(t)$ be the corresponding output. The system $\mathcal S$ is time-invariant if, for any time shift $\tau$,

$$\mathcal S \left\{x(t-\tau)\right\} = y(t-\tau)$$

A common violation of the time-invariance condition occurs when a system has non-zero initial conditions.

## Related system properties
### Causality
### Stability

## Properties of LTI systems

An LTI system is [uniquely characterized by its impulse response](#impulse-response-and-convolution). The [Frequency response](#frequency-response) of an LTI system is the Fourier transform of its impulse response.

### Impulse response and convolution

````{panels}
:header: text-center
**Continuous time**
^^^
A continuous time impulse, (also known as the Dirac delta) can be defined as a limit.

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

```{admonition} Eigenfunction
If application of the system $\mathcal S$ to the signal $x(t)$ simply results in a scaling ( i.e. $\mathcal S \{x(t)\} = \lambda x(t) $ ) then we say that $x(t)$ is an eigenfunction of the system. 
```

````{panels}
:header: text-center
**Continuous time**
^^^
If the input to an LTI system is a complex exponential $x(t) = e^{j \omega t}$, then the corresponding output is

$$ y(t) = H(j \omega) e^{j\omega t} $$

where $H(j\omega)$ (called the frequency response) is the Fourier transform of the impulse response

$$H(j\omega) = \mathcal F \{ h(t) \}$$

---

**Discrete time**
^^^
If the input to an LTI system is a complex exponential $x[n] = e^{j \omega n}$, then the corresponding output is

$$ y[n] = H(e^{j\omega}) e^{j\omega n} $$

where $H(e^{j\omega})$ (called the frequency response) is the Discrete-time Fourier transform of the impulse response

$$H(e^{j\omega}) = \text{DTFT} \{ h[n] \}$$

````

### Magnitude and phase response



## Frequency selectivity

### Lowpass
### Highpass
### Bandpass
### Bandstop
### Notch
### All-pass

