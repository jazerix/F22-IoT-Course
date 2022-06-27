# Toolchain

Benjamin
## Signals

Analog signals are usually the evolution of a metric (time --> value). Normally in signals it is **Voltage** that is measured.

**Voltage**
* Definition: *A difference in electrical potential*
* Implication: The metric relates to two points in a circuit

**Transducers**
* Definition: *A device which converts energy from one form to another*
* Inputs such as Light, Heat, Force, EM Radiation...
* Outputs such as: Electrical signal (Voltage)

**Example: Thermistor**
* A thermistor is a component whose resistivity is a reversible function of the temperature
* Usually measured with the voltage divider equation
* Assumption: high temperatures = high resistance
  * High V<sub>out</sub> --> High R<sub>2</sub>--> High temperature
  * Low V<sub>out</sub> --> Low R<sub>1</sub>--> Low temperature


**General Data Collection Pipeline:**
We want to convert a analog output to a digital output
* Continouos signal --(Sampler)->
* Discrete signal --(Interpolator)->
* Reconstructed signal

## Basic Output
Devices can output several types of signals:
* Digital
* Analog (Using Digital to Analog Converter (DAC))
* PWM (Digital but with limited duty cycles)

## Basic Input
* Digital
* Analog (Using Analog to Digital Converter (ADC))

## Serial Communication
Definition: *Transferring a chunk of data one bit after the other*

Several ways to do:
* SPI
* I2C
* RS232 (subject of the lecture)

## RS232 Frame Format
Simplest form: Three wire protocol:
* Communication in one direction,
* Communication in the other direction,
* Ground

**Format**
* 1 start bit (HIGH)
* a character spanning 7-8 bits
* an (optional) parity bit
* number of stopbits (1-3) (LOW)

i.e.
(start)(character)(parity)(stop)

## Working with incoming data
Decisions with arriving data:

**Choices on format**
1. Machine-readable: simple to parse
2. Human-readable: simple to debug

**Choices on dispatch mechanism**
1. Lookup using table
2. Lookup using map
3. Chain of branches
4. Deterministic finite automaton