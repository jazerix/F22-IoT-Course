# Sampling physical phenonoma

Daniel


Data collection sker om regel igennem en sampler, hvor man får et discrete signal, som man kan bruge en interpolator på for at reconstruct signalet. 

## Sampling
    - Sampling interval er den tid det tager mellem to samples
    - Sampling frequency / sampling rate er det gennemsnitlige antal af samlings man får hvert sekund

## Sample and Hold Method
    - Flush, Drain the charge og the cpacitor by connecting it to ground
    - Wait, Make sure that input is not connected to ground
    - Sample Connect the capacitor to the input. This will charge the capacitor over time
    - Hold, Given a large enough sample time the capacitor is charge to a voltage matching the input
    - Compare, This charge can then be compared to multiple known values, once for each output bit

- Compare step
    - Der sammenlignes én gang pr. bit
    - Known values (representing bits) kan vises som linear ADC eller logarithmic ADC pattern (Decibel er f.eks. logaritmisk)

## Noise og SNR
Noise kommer tit fra mange sources. Sensor er oftest noisy, analog electrical signals opsamler noise from electromagnetical signals, AD conversion skaber noise.

Den naturlige noise der findes i det miljø man er i kaldes for noise floor. Signal to noise ratio (SNR) fortæller os hvor stor en del af vores signal der består af noise.

Hvad sker der hvis man tager average af to samples?
- Signalet bliver fordoblet
- Nogle typer af noise bliver cancelled out
- SNR stiger

## Sampling Theorem
How frequent do you have to sample to reconstruct a signal?
    - Twice as fast as the fastest frequency contained in the original signal

## Resampling
En timeseries er en mapping fra tid til values. Når man skal adapt frequency af en timeseries, så kan man vælge at resample på følgende måder
- Downsampling, hvor man laver en ny timeseries til at repræsentere det samme signal ved at bruge færre samples
- Upsamling, hvor man laver en ny timeseries til at repræsentere det samme signal ved at bruge flere samples

Dette introducere fejl, hvor disse fejl bl.a. kan være
- Cutting off extreme values
- Removing fluctuations

## Outlier
En outlier er et sample som der ligger langt væk fra den normale distribution af samples. En black swan er en outlier der er fjernet, som efterfølgende viste sig at være significant. 