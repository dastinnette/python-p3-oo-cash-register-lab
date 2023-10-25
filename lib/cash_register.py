#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, item, price, quantity=1):
    self.previous = (price * quantity)
    self.total += (price * quantity)
    
    while quantity > 0:
      self.items.append(item)
      quantity -= 1

  def apply_discount(self):
    if self.discount != 0:
      self.total -= (self.discount/100) * self.total
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total -= self.previous
    