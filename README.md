# Delay
Delay neuron for kalliope
## Synopsis

Delay a neuron or a synapse

## Installation
```bash
kalliope install --git-url https://github.com/corus87/delay-neuron
```

## Options


| parameter    | required | choices | comments                                      |
|--------------|----------|---------|-----------------------------------------------|
| seconds      | yes      |integer  | time to delay the neuron                      |
| synapse      | no       |string   | start synapse after x seconds (runs as thread)|



## Synapses example
```
  - name: "turn-on-off"
    signals:
      - order: "Turn on wait and turn off"
    neurons:
      - gpio:
          set_pin_high:
            - 17
      - delay:
          seconds: 5
      - gpio:
          set_pin_low:
            - 17          
            
  - name: "turn-off-after"
    signals:
      - order: "turn off the lights later the night"
    neurons:
      - delay:
           seconds: 600
           synapse:  "light-off"

  - name: "light-off"
    signals:
      - order: "turn off the lights now"
    neurons:
      - gpio:
          set_pin_low:
            - 17
            - 18
            - 22
            - 27

```
