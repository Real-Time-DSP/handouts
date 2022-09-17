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

Note that if the window function we choose has a finite width of $L$, then the integral bounds in the STFT can be equivalently written as:

$$\begin{align}
\text{STFT} \{x(t) \} &= \mathscr F \{ x(\tau) w_L(\tau-t) \} \\
&= \int_{\tau=-L/2}^{L/2}{ x(\tau)w(\tau-t) e^{-j 2\pi f \tau}d\tau}
\end{align}$$

At each time $t$, this is equivalent to finding the *Fourier series* coefficients of the signal created by taking the *length $L$ periodic extension* of $x(\tau)w_L(\tau-t)$

In other words, once the window is applied, the Fourier transform is equivalent to a Fourier series. This fact will be useful as we move on to the discrete version of the STFT.

### Discrete STFT

The discrete version of the STFT replaces the Fourier transform with the DTFT. However, the discrete window functions $w[n]$ that are typically used have finite width,

$$\begin{align}
\text{STFT} \{x[n] \} &\equiv X(t, f)\\
&= \mathscr F \{ x(\tau) w(\tau-t) \}\\
&= \int_{\tau=-\infty}^{\infty}{ x(\tau)w(\tau-t) e^{-j 2 \pi f \tau}d\tau}
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

If we want to work with a discrete signal $x[n]$, then the Fourier transform becomes a discrete-time Fourier transform (DTFT).


To perform the discrete version of the STFT, we must first choose a *discrete* window function $w[n]$. The window function can either be designed for a specific application or we can just use a sampled version of a continuous window function like the rectangular or Hann window.

We divide the signal $x[n]$ into segments which are the same length as w[n], then compute the discrete fourier transform of each windowed segment $x[n]w[n-k]$. For each segment, we get a vector containing a frequency domain representation of $x[n]$ near $k$. Repeating this for many values of $k$ results in a two-dimensional (time,frequency) representation of the signal.

Since the Fourier transform is, in general, complex-valued, we rarely use the STFT directly. Instead, it is common to separate it into it's magnitude and phase. The plot constructed from the magnitude of the STFT is called the magnitude spectrogram.

## Filter banks

Although the STFT has become ubiquitous for analyzing audio, another method existed long before computers and fast Fourier transform algorithms.

![](img/helmholtz.svg)

Much of the theory of time-frequency analysis was developed by Helmholtz, who built what would now be considered an analog 'spectrum analyzer'. At its core, it consists of an array of filters, each of which respond to a narrow range of frequencies.

The Haar decomposition can be considered a two-channel filter bank that decomposes the signal into a high-pass and a low-pass component. By recursively application of this process, we can divide the signal into arbitrarily many bands while maintaining a simple process to recover the signal. This is another way to construct a time-frequency distribution, and is the simplest example of a discrete wavelet transform.