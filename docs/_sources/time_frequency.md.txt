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

## The short-time Fourier transform

A common method for constructing a time-frequency distribution is the magnitude spectrogram, which is in-turn computed using a variation of the short-time Fourier transform (STFT)

### Continuous STFT

The continuous-time STFT of a one-dimensional signal $x(t)$ is a two-dimensional (time and frequency) representation.

Recall the definition of the conventional Fourier transform:

$$\begin{align}
\mathscr F \{ x(t) \} &\equiv X(\omega) \\
&= \int_{t=-\infty}^{\infty}{ x(t) e^{j\omega t}dt}
\end{align}$$

$x(t)$ is a function of time but $X(\omega)$ is not because we've integrated over all time from $-\infty$ to $\infty$.

If we multiply $x(t)$ by a **window function** centered on $\tau$ before taking the Fourier transform, then the result would be similar to limiting the bounds of integration to the interval $\left[ \tau-\sigma, \tau + \sigma \right]$

```{admonition} Window functions
A window function $w(t)$ is any function designed to 'focus' on a segment of a signal by suppressing everything outside of the window. Usually, $w(t)$ is symmetric about the origin. If we want to focus on a signal $x(t)$ near the origin then we use the product $x(t)w(t)$. To focus on $x(t)$ at some location other than the origin $\tau$, we would shift the window function first, i.e. use the product $x(t)w(t-\tau)$
```

::: {panels}
:container: container-lg pb-4
:header: text-center

**Rectangular window**
^^^

$$w(t)=\sigma^{-1/2} \text{rect} \left(\frac{t}{\sigma} \right)$$

---

**Gaussian window**
^^^

$$w(t) = A \exp {\frac{-t^2}{2\sigma^2}} $$

Where $A=2^{1/2}\sigma^{-1/2}\pi^{-1/4}$ so that the window has unit energy.

---

**Lanczos window**
^^^

$$ w(t) = \text{sinc} \left( \frac t \sigma \right) \text{rect} \left(\frac{t}{\sigma} \right)$$

---

**Hann window**
^^^

$$w(t) = \frac{1}{2}\left[1+\cos\left(\frac{2\pi t}{\sigma}\right) \right]\text{rect} \left(\frac{t}{\sigma} \right)$$

:::


In contrast to the conventional Fourier transform, the STFT uses a window function centered on $\tau, w(t-\tau)$ to keep the time variable $t$ while also introducing the frequency variable $\omega$.

$$\begin{align}
\text{STFT} \{x(t) \} &\equiv X(\tau, \omega)\\
&= \mathscr F \{ x(t) w(t-\tau) \}\\
&= \int_{t=-\infty}^{\infty}{ x(t)w(t-\tau) e^{j\omega t}dt}
\end{align}$$

### Discrete STFT

To perform the discrete version of the STFT, we choose a discrete window function $w[n]$. The window function can either be designed for a specific application or we can just use a sampled version of a continuous window function like the rectangular or Hann window.

We divide the signal $x[n]$ into segments which are the same length as w[n], then compute the discrete fourier transform of each windowed segment $x[n]w[n-k]$. For each segment, we get a vector containing a frequency domain representation of $x[n]$ near $k$. Repeating this for many values of $k$ results in a two-dimensional (time,frequency) representation of the signal.

Since the Fourier transform is, in general, complex-valued, we rarely use the STFT directly. Instead, it is common to separate it into it's magnitude and phase. The plot constructed from the magnitude of the STFT is called the magnitude spectrogram.

## Filter banks

Although the STFT has become ubiquitous for analyzing audio, another method existed long before computers and fast Fourier transform algorithms.

![](img/helmholtz.svg)

Much of the theory of time-frequency analysis was developed by Helmholtz, who built what would now be considered an analog 'spectrum analyzer'. At its core, it consists of an array of filters, each of which respond to a narrow range of frequencies.

The Haar decomposition can be considered a two-channel filter bank that decomposes the signal into a high-pass and a low-pass component. By recursively application of this process, we can divide the signal into arbitrarily many bands while maintaining a simple process to recover the signal. This is another way to construct a time-frequency distribution, and is the simplest example of a discrete wavelet transform.