#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from typing import Union


class ProgressBar:
  def __init__(self, init_values: Union[float, tuple]):
    # define a progressbar object with either an int (percentage) or a tuple (current_value,max_value)
    if isinstance(init_values,float):
      self._percent = init_values
      self._value = self._percent
      self._max = 100.0

    elif isinstance(init_values,tuple):
      if len(init_values) != 2:
        raise ValueError
      self._value, self._max = init_values
      self._percent = (self._value*100)/self._max

############################
  @property
  def percent_progression(self):
    return self._percent

  @percent_progression.setter
  def percent_progression(self, value: Union[float,str]):
    if isinstance(value,str):
      value = value.lstrip().rstrip()
      if value[0] == "+":
        self._percent += float(value)
      elif value[0] == "-":
        self._percent -= float(value)
    elif isinstance(value,float):
      self._percent = value
    else:
      raise TypeError

    self._value = self._percent

  @percent_progression.deleter
  def percent_progression(self):
    del self._percent, self._value, self._max
    return None

############################
  @property
  def value_progression(self):
    return (self._value, self._max, self._percent)

  @value_progression.setter
  def value_progression(self, value: int):
    self._value = value
    self._percent = (self._value*100)/self._max

  @value_progression.deleter
  def value_progression(self):
    del self._percent, self._value, self._max
    return None
