# Smart Rockets Genetic Algorithm

A rocket genetic algorithm built in Python using **Pygame**. This project demonstrates how a population of independent rockets can "learn" to navigate toward a target over successive generations using a **Genetic Algorithm (GA)** consisting of selection, crossover, and mutation.

---

## Features

* **Genetic Algorithm Implementation:** Features realistic mating pools, crossover, and random mutation.
* **Dynamic Fitness Evaluation:** Rockets are rewarded based on how close they get to the target and how quickly they manage to get there.
* **Visual Highlights:** The rocket closest to the target in the current generation is highlighted in **green** to track the best-performing DNA in real-time.
* **Generation Tracker:** A counter tracking the generation count.
* **Time dependent fitness:** In early generations of genetic algorithms, a common problem is getting stuck in **local optima**, where rockets find a "good enough" path (like crashing down and then move up to hit the target) and the population stops evolving better paths. To solve this, the fitness function incorporates a time-penalty factor

---

## How It Works

Each rocket has a brain (`DNA`) consisting of a sequence of 300 force vectors (acceleration coordinates). 

1. **Evaluation:** Once all rockets complete their 300 frames of movement, their `fitness` is calculated based on their distance to the target.
2. **Selection:** Rockets are added to a mating pool with a frequency proportional to their fitness scores (higher fitness = higher chance of reproducing).
3. **Crossover:** Two parents are chosen at random from the pool, and their genes are split and combined at a random midpoint to create a child.
4. **Mutation:** There is a small, random chance ($1\%$) that any given force vector in a child's DNA will mutate into a completely new direction diversity.

---

## Prerequisites

Make sure you have Python and `pygame` installed. 

```bash
pip install pygame
