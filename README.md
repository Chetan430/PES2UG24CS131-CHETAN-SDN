CHETAN, PES2UG24CS131, SDN REPORT

# SDN using Mininet and POX Controller

## Overview

This project demonstrates SDN using Mininet and POX.

## Custom Controller Code
A simple Python-based POX controller is implemented to handle packet forwarding.


## Topology

Single switch with 3 hosts.

## Steps

### Run Controller

cd ~/pox
./pox.py forwarding.l2_learning host_discovery openflow.of_01 --port=6633

### Run Mininet

sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633

### Test

pingall

## Output

0% packet loss (all hosts connected)
