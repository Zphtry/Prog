import random as rand
import matplotlib.pyplot as plt
import numpy as np


p_success = .8
p_loose   = .2

success_edge = 4

n_steps = 100

tests_num = 10


def next_step():
  return 1 if rand.random() <= p_success else 0

def win_for_num(n):
  [next_step() for i in range(n)].count(1) >= success_edge

def prob_for_num(n):
  sum([win_for_num(n) for i in range(tests_num))] / tests_num

probs = []

for i in range(5, n_steps):
  probs.append(prob_for_num(i))

print(probs)
