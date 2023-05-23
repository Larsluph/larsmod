#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil


def _get_addrs(addr_type: str = None) -> dict:
    """
    fetch all addresses with family type {addr_type}

    :param addr_type:  MAC="AF_LINK", IPv4="AF_INET", IPv6="AF_INET6"
        If None, it will return: {adapter_name: {family: address, ...}, ...}
        else, it will return: {adapter_name: address, ...}
    """
    addresses = psutil.net_if_addrs()  # get all adapter data
    nic_name = list(addresses.keys())  # separate adapters' name
    nic_addrs = dict()
    v = list(addresses.values())  # temporary store adapters' data
    for x in range(len(v)):  # for each adapter
        temp = dict()
        for y in range(len(v[x])):  # for each addresses
            if addr_type is None:
                temp[v[x][y].family.name] = v[x][y].address
            else:
                if v[x][y].family.name == addr_type:  # save only addr_type
                    nic_addrs[nic_name[x]] = v[x][y].address
        nic_addrs[nic_name[x]] = temp

    return nic_addrs


def get_ip4_addrs() -> dict:
    """
    fetch all IPv4 adresses on the registered adapters
    
    returns: {adapter_name : IPv4}
    """
    return _get_addrs("AF_INET")


def get_ip6_addrs() -> dict:
    """
    fetch all IPv6 adresses on the registered adapters

    returns: {adapter_name : IPv6}
    """
    return _get_addrs("AF_INET6")


def get_mac_addrs() -> dict:
    """
    fetch all MAC adresses on the registered adapters

    returns: {adapter_name : MAC}
    """
    return _get_addrs("AF_LINK")
