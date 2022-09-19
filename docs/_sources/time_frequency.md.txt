<style>
@media print {
    .pagebreak { page-break-before: always; } /* page-break-after works, as well */
}
</style>

# Time-Frequency Analysis

An example of a joint time-frequency signal representation is standard musical notation.

![](img/music.png)

Imagine that instead of this notation, we used a purely time-domain description that describes the shape of the acoustic waveform.

![](img/time.svg)

Although the musician might be able to make out the rhythm and intensity clearly, it would be impossible to determine exactly which notes to play.

Now imagine that we used a purely frequency domain description, e.g. the Fourier transform.

![](img/freq.svg)

This would show which notes to play, but it would be impossible to know when to play them.

In many applications (especially audio) the joint representation can reveal the most important aspects of a signal which might be hidden in the time or frequency domains alone.

Consider two more examples:

1. The sound of a bird chirping

2. The ping from marine sonar system

<video width="740" height="400" style="float: right;" controls src="_static/chirp.mp4" />"

![](img/chirp.svg)

<video width="740" height="400" style="float: right;" controls src="_static/ping.mp4" />"

![](img/ping.svg)

Although all three representations (time-domain, frequency-domain, and joint time-frequency) contain equivalent information, it is clear that the joint representation has several advantages.

Before we can dig deeper, we must take a step back and understand how time-frequency distributions like the ones above are constructed.

## The short-time Fourier transform (STFT)

A common method for constructing a time-frequency distribution is the magnitude spectrogram, which is in-turn computed using a variation of the short-time Fourier transform (STFT)

### Continuous STFT

The continuous-time STFT of a one-dimensional signal $x(t)$ is a two-dimensional (time and frequency) representation $X(t,f)$.

Recall the definition of the conventional Fourier transform:

$$\begin{align}
\mathscr F \{ x(t) \} &\equiv X(f) \\
&= \int_{t=-\infty}^{\infty}{ x(t) e^{-j 2\pi f t}dt}
\end{align}$$

$x(t)$ is a function of time but $X(f)$ is not because we've integrated over all time from $-\infty$ to $\infty$.

In contrast, the STFT uses a window function $w(\tau)$ to keep the time variable $t$ while also introducing the frequency variable $f$.

$$\begin{align}
\text{STFT} \{x(t) \} &\equiv X(t, f)\\
&= \mathscr F \{ x(\tau) w(\tau-t) \}\\
&= \int_{\tau=-\infty}^{\infty}{ x(\tau)w(\tau-t) e^{- j 2\pi f \tau}d\tau}
\end{align}$$

```{admonition} Window functions
A window function $w(t)$ is any function designed to 'focus' on a segment of a signal by suppressing everything outside of the window. Usually, $w(t)$ is symmetric about the origin. If we want to focus on a signal $x(t)$ near the origin then we use the product $x(t)w(t)$. To focus on $x(t)$ at some location $a$ instead of the origin, we shift the window function first, i.e. we use the product $x(t)w(t-a)$. We usually choose the amplitude $A$ of a window so that it has unit energy, i.e. $\int{w^2 (t) dt} = 1$. The width of the window $\sigma$ is an important parameter since it controls the trade-off between time and frequency resolution. Some common window functions are shown below.
```

::: {panels}
:container: container-lg pb-4
:header: text-center

**Rectangular window**
^^^

$$w(t)= A \text{ rect} \left(t/2 \sigma \right)$$

![](img/window_rect.svg)

---
**Gaussian window**
^^^

$$w(t) = A e^{-t^2/2\sigma^2} $$

![](img/window_gaussian.svg)

---

**Lanczos window**
^^^

$$ w(t) = A \text{ sinc} \left( \frac t \sigma \right) \text{rect} \left(\frac{t}{2\sigma} \right)$$

![](img/window_lanczos.svg)

---

**Hann window**
^^^

$$w(t) = \frac{A}{2}\left[1+\cos\left(\frac{\pi t}{\sigma}\right) \right]\text{rect} \left(\frac{t}{2\sigma} \right)$$

![](img/window_hann.svg)

:::

```{admonition} Equivalence of Fourier transform and Fourier series for windowed signals

Note that if the window function we choose has a finite width of $L$, then the integral bounds in the STFT can be equivalently written as:

$$\begin{align}
\text{STFT} \{x(t) \} &= \mathscr F \{ x(\tau) w_L(\tau-t) \} \\
&= \int_{\tau=-L/2}^{L/2}{ x(\tau)w_L(\tau-t) e^{-j 2\pi f \tau}d\tau}
\end{align}$$

At each time $t$, this is equivalent to finding the *Fourier series* coefficients of the signal created by taking the *length $L$ periodic extension* of $x(\tau)w_L(\tau-t)$.

In other words, once the window is applied, the Fourier transform is equivalent to a Fourier series.

The same is true in discrete time. If we first apply a finite length window $w_L[n]$, then the discrete-time Fourier transform (DTFT) is equivalent to the discrete Fourier transform (DFT).

```

### Discrete STFT

The discrete version of the STFT replaces the Fourier transform with the discrete-time Fourier transform (DTFT). However, the discrete window function $w_L[n]$ is typically causal (instead of centered on the origin) and has finite length $L$. As a result of the finite length, the DTFT is equivalent to a discrete Fourier transform (DFT), and the discrete STFT $X[n,k]$ is sampled both time (indexed by $n$) and in frequency (indexed by $k$).

$$\begin{align}
\text{STFT} \{x[n] \} &\equiv X[n,k]\\
&= \text{DTFT} \{ x[m]w_L[m-n] \}\\
&= \sum_{m=-\infty}^{\infty}{ x[m] w_L[m-n] e^{-j 2 \pi f m}} \\
&= \sum_{m=0}^{L-1}{ x[m] w_L[m-n] e^{-j 2 \pi k m / L}} \\
&= \text{DFT} \{ x[m]w_L[m-n] \}
\end{align}$$

```{admonition} Sampling and the DTFT

The impulse train with sampling period $T_s$ is defined as

$$Ш_{T_s}(t)=\sum_{k=-\infty}^{\infty}{\delta(t-kT_s})$$

The fourier transform of an impulse train is another impulse train.

$$\begin{align}
\mathscr F \{ Ш_{T_s}(t) \} &= \frac {1}{T_s} Ш_{1/T_s}(f) \\
&=  f_s Ш_{f_s}(f)
\end{align}$$

The operation of sampling can be modeled as multiplication with an impulse train.

$$x[n] = x(t) \cdot Ш_{T_s}(t)$$

The fourier transform of a sampled signal is called the discrete-time Fourier transform (DTFT).

$$\begin{align}
\text{DTFT}_ \{x[n] \} &= \sum_{n=-\infty}^{\infty}{x[n] e^{-j 2\pi f n}} \\
&= \mathscr F \{ x(t) Ш_{T_s}(t) \} \\
&= \frac{1}{2\pi} \mathscr F \{ x(t) \} * \mathscr F \{ Ш_{T_s}(t) \} \\
&= \frac{f_s}{2\pi} X(f) * Ш_{f_s}(f) 
\end{align}$$

```
In other words, to construct the discrete STFT, we perform 3 steps:

1. Divide the signal $x[n]$ into segments of length $L$
2. Multiply each segment by the window function $w_L[n]$ 
3. Compute the discrete Fourier transform of each windowed segment using the fast Fourier transform (FFT) algorithm.

Since the Fourier transform is, in general, complex-valued, we rarely use the STFT directly. Instead, it is common to separate it into it's magnitude and phase. The plot constructed from the magnitude of the STFT, like the ones shown earlier, is called the **magnitude spectrogram**.

## Filter banks

Although the STFT has become ubiquitous for analyzing audio, another method of of time-frequency analysis existed long before computers and fast Fourier transform algorithms: the **filter bank**.

![](img/helmholtz.svg)

An example of an analog filter bank used for time-frequency analysis, called the *Koenig flame apparatus*, is shown above. It utilizes an array of acoustic bandpass filters, called *Helmholtz resonators*, to visualize the frequency content of incoming sound using a rotating mirror to display the flame manometers which are connected to the array of Helmholtz resonators.

Even in the realm of digital implementation, the filter bank approach to time-frequency analysis has some advantages. When we use the DFT for frequency analysis, we are limited to equally spaced frequency bins and an average latency of $L/2$ samples. However, we can design the array of bandpass filters in a filter bank to have whatever spacing, frequency response, or delay characteristics necessary for our application.

If we wanted to produce a similar number of frequency bands as we would typically get from the DFT (anywhere from tens to thousands of bands), then we would need to apply tens or thousands of discrete-time filters in parallel. This gets expensive very quickly! Fortunately, there is a more efficient method.

### Multirate filter banks

To demonstrate the theory underlying multirate filter banks, let us consider one of the simplest examples: the **Haar decomposition.** 

#### Haar Decomposition

In 1909, mathematician Alfréd Haar used a procedure which we would now call a *discrete wavelet transform* using sums of differences of a list of numbers.

Consider the finite length signal $x[n]$ below consisting of eight samples:

| $x[0]$ | $x[1]$ | $x[2]$ | $x[3]$ | $x[4]$ | $x[5]$ | $x[6]$ | $x[7]$ |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 7    | 1    | −13  | 20   | 4    | 7    | −18  | 5    |

The transformation we will apply consists of creating two other signals $s[k]$ and $d[k]$ by taking sums and differences of adjacent samples from $x[n]$. However, the signals $s[k]$ and $d[k]$ will both half the length of the original signal $x[n]$.

$$s[k] = x[2k] + x[2k+1]$$
$$d[k] = x[2k+1] - x[2k]$$

| $d[0]$ | $d[0]$ | $s[1]$ | $d[1]$ | $s[2]$ | $d[2]$ | $s[3]$ | $d[3]$ |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| 7+1    | 1−7    | −13+20 | 20+13  | 4+7    | 7−4    | −18+5  | 5+18   |
| 8      | −6     | 7      | 33     | 11     | 3      | −13    | 23     |

Although these equations look similar to an LTI system specified by a difference equation, these relationships do not constitute LTI systems because they include **downsampling operations**

```{admonition} Upsampling and downsampling
```

We can equivalently express these two systems in terms of convolution (i.e. application of an LTI filter) and a downsampling operation.

$$s[k] = \downarrow_2 \left(x[n]*\left(\delta[k] + \delta[k-1]\right)\right)$$
$$d[k] = \downarrow_2 \left(x[n]*\left(\delta[k] - \delta[k-1]\right)\right)$$

This transformation, the Haar decomposition, can be considered a two-channel filter bank that decomposes the signal into a high-pass and a low-pass component, followed by downsampling by two. By recursive application of this process, we can divide the signal into arbitrarily many bands while maintaining a simple process to recover the signal.

```{admonition} Frequency response of two-sample sum and difference
```

In particular, the $n$th sample of the original signal can be recovered using the following procedure:

$$\begin{align}
\hat x [n] &= \left( \uparrow_2 s[k] \right) * \left( \frac 1 2 \delta[n-1] - \frac 1 2 \delta[n] \right) \\
&+ \left( \uparrow_2  d[k] \right) * \left(\frac 1 2 \delta[n-1] + \frac 1 2 \delta[n] \right)
\end{align}$$