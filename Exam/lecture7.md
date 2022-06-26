# Annotating identity time and space

Daniel

## Identity

### Naming
Dette handler ikke om at navngive noget, men at kunne reference noget (en pointer). 

### Identity Management
Identity er et name. Her skal man kunne navngive devices, så den datastream der tilhører et device giver mening. Et device kan godt have flere identities, f.eks. hvis den både bruger WiFi og bluetooth. 

### Sources of Identity
Et par populære er
- Unique device number (serial)
- User-provided
- (Physical) location-derived (coordinate set)
- Network-derived (logical location) (dns)
- Context-derived (kombination af hvad det er, hvor det er og hvad der sker rundt om den)

### Point of Identification
Hvor hører identity af en node til?
- Node (self-aware)
- Cloud ("Central" knowledge)
- Private (Stored with the user)

Her handler det meget om, at der er forskellige konsekvenser med hvem der kender ens identity.

## Time

### Keeping Track of Time
Når er device kører, så tæller den clock ticks, hvilket kan give et timestamp siden boot. 

### Point of Timestamping
1. When sampling (on device)
2. When transmitting (on device)
3. When receiving (on gateway)
4. When pushing to cloud (on gateway)
5. When receiving in the cloud (in cloud)
6. When receiving from the cloud (from cloud)

Timestamping giver kun mening på et device, hvis der er en form for synkronization på den, så den reelt ved hvad tid er. Dette er et high quality timestamp. Hvis den ikke har en idé om tid, så kan den godt lave et timestamp, som der vil være et stigende tal, men et stigende tal der ikke fortæller nogen kontekst om hvad tiden reelt er.

### Sources of Time
På et device har vi
1. Offset (relative time)
2. Global Navigation Satellite System (GNSS)
3. USB cable on startup
4. Downstream push
5. In-channel broadcast
6. Backchannel broadcast
7. Network Time Protocol (NTP)

## Space

### Triangulation of Position

Dette handler om at udregne distance til nogle kendte punkter for at finde ud af hvor man selv er. Når man snakker om distance her, så mener man egentlig signal strength, når man ikke er på GPS.

### Sources of Position
Direkte sources er
1. Hardcoded in firmware or flash
2. GPS/GLONASS/Galileo/BeiDou
3. Downstream push
4. USB cable on startup

Indirekte sources er (kræver triangulation)
1. Signal strenghts of radio signals from known positions
