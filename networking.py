#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import psutil

def get_net_addrs() -> dict:
  "fetch all IPv4 adresses on the registered adapters"
  addresses = psutil.net_if_addrs() # get all adapter data
  nic_name = list(addresses.keys()) # separate adapters' name
  nic_addrs = []
  v = list(addresses.values()) # temporary store adapters' data
  for x in range(len(v)): # for each adapter
    for y in range(len(v[x])): # for each addresses (MAC: AF_LINK, IPv4: AF_INET, IPv6: AF_INET6)
      if v[x][y].family.name == 'AF_INET': # save only IPv4
        nic_addrs.append(v[x][y].address)

  return {name: nic_addrs[nic_name.index(name)] for name in nic_name}
