#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value=value
  @property
  def value(self):
    self._value=value
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value=value
    else: 
      print("The value must be a string.")
  def is_sentence(self):
    if self._value[-1]==".":
      return True
    else:
      return False

  def is_question(self):
    if self._value[-1]=="?":
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value[-1]=="!":
      return True
    else:
      return False

  def count_sentences(self):
    value=self._value
    for punc in ["!", "?"]:
      value=value.replace(punc, ".")
    if value=="":
      return 0
    else:
      lists = value.split(". ")
      return len(lists)