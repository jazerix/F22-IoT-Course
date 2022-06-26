# To infinity and beyond
**Everything measured is a voltage, and that is analog and not always pretty.**

In a ADC, the Multiplexer allows us to choose an input channel (measure voltage on a pin)

**General Data Collection Pipeline:**
* Continouos signal --(Sampler)->
* Discrete signal --(Interpolator)->
* Reconstructed signal


**RS232 Frame format (Serial standard)**
* 1 start bit (HIGH)
* a character spanning 7-8 bits
* an (optional) parity bit
* number of stopbits (1-3) (LOW)

**Performance Space**
* Three-way tradeoff between
  * Power
  * Throughput
  * Range


**Publish Subscribe**
* Routing Layer
* * Makes sure that packets are placed in correct topic queue
* Configuration
* * Packets are forwarded according to the configuration

* Examples
  * Kafka
    * Subscribe to a specific topic 
  * MQTT
    * Have a pattern over the topic
  * Rarely used
    * sMAP -> no commercial appliances yet according to Aslak
  * "Data Portal"
    * subscribe using query over ontological model (Aslaks own)




**FUTURE (10ECTS)** 
* Why Elixir
* * Responsiveness 
* * Convenient concurrency model
* * no stop-the-world garbage collection --> More consistent performance
* Elixir code can be organized in modules
* Elixir has an interactive mode, the interpreter command is called **iex**
* Elixir processes are run essentially run in a shell/"sandbox"


**BEAM**
* Combination of Erlang and Elixir
* Who uses BEAM?
  * Discord (5M users)
  * Facebook (chat services)
  * WhatsApp
  * *If someone is succesful an doing routing that requires scalability, availability and consistent low latency, they are likely relying on being*
* Basic Types in BEAM
  * integer, float, boolean, string, tuple
  * atom: Essentially a global enum, Atoms are names that start with a colon
* Inspection
* any Elxir term can be inspected using the **i/1** function:
**iex(1)>** *i "Hello, World"*
 gives data type, byte size, description etc. 

 * Unavoidable truth:
   * *The unavoidable truth about software running in production is that things will (eventually) go wrong."* - The Elixir Website
   * However, Elixir program or system will already have supervisors configured to deal with crashes
   * Therefore, the best choice ends up simply letting it crash, so that its supervisor will reload it with a fresh state, without interfering without the (millions) other processes.
* "Defensive vs. Offensive Programming"
  * When crashing becomes acceptable it loosens the need for guards and logic for handling error conditions in the codebase.
  * Responsible programmers doesn't have to be defensive against errors
  * Also gives a very clean codebase

**Nerves (framework)**
* Framework for programming Raspberry Pi (and up) hardware.
* Builds on a minimal Linux kernel
* Boots straight into a BEAM virtual machine
* Firmware updates exists and can often be pushed as hot updates (NervusHub)

This means that:
1. You have a cluster of (software) VMs that spans cloud, fog and edge.
2. That logic can be shifted between these layers as needed
3. The interfaces between these layers are indistinguishable from your native API (instead of having to rely on a heavy and/or inflexible transport)
4. That you can easily move logic to the data

**!!!!EXAM!!!!**
* Individual 20 min
* More than welcome to refer to practical experiences, and this is particularly relevant when providing examples, i.e.
  * Semester project
  * Exercises from the course
  * Anything else course-relevant
  * (NOT REQUIRED)
* "Bring it up, and then we can talk about that"
* During the examination, a subset of the curriculum will be covered
* Hypotheticals: "We going to do this and this and this - what kind of technologies are we looking to use" - Aslak
