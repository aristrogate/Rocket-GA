# Smart Rockets Genetic Algorithm 🚀

A fun little Python project (using **Pygame**) where a bunch of rockets slowly *teach themselves* how to fly to a red target. Nobody tells them the way, they figure it out over many "generations", just like evolution in nature.

---

## What is happening on screen?

- 50 rockets launch from the bottom of the window.
- A red dot sits near the top, that's the target.
- At first, the rockets fly around like confused bugs. That's normal! Their moves are completely random.
- After every round, the best rockets are chosen to make the next generation, and the kids fly a little smarter.
- Give it a few generations and you'll see the whole swarm start homing in on the target.

---

## Features (in plain words)

* **Rockets learn by evolution:** Good rockets pass their "DNA" to the next generation. Bad rockets slowly disappear.

* **Every rocket has DNA:** A rocket's DNA is simply a list of 300 tiny forces. One force is used every frame.

* **Fitness score :** After each round, every rocket gets a score:
  - The **closer** it got to the target, the **higher** the score.
  - Rockets that actually **touch the target** get a big bonus.
  - Faster is better - a rocket that reaches the target quickly earns a **bigger bonus** than a slow one. Hitting it at frame 100 pays about 3x more than hitting it at frame 300.

* **Closest-distance memory:** A rocket is judged by the *closest* it ever got to the target during its flight, not just where it ended up. So a rocket that flew right past the target still gets credit for getting near it.

* **Parent picking (Selection):** Rockets with better scores have a better chance of being picked as parents.

* **Mixing parents (Crossover):** A child rocket gets the first part of its flight plan from parent A and the rest from parent B. The split point is random, and the child is guaranteed to get genes from both parents.

* **Random surprises (Mutation):** Each move in a child's DNA has a small **1% chance** of being replaced by a brand-new random move. This keeps the population from all becoming identical copies and helps them discover new tricks.

* **The champion never dies (Elitism):** The single best rocket of each generation gets copied into the next generation *unchanged*. This way the population can never "forget" its best flight plan so far.

* **Green rocket = current best:** At any moment, the rocket closest to the target is drawn in **green** so you can easily spot the star of the show.

* **Generation counter:** The number in the top-left corner tells you how many rounds of evolution have happened.

* **Time-based bonus (why it matters):** A common problem in these simulations is rockets finding a "good enough" but silly path, like flying down first and then curving back up to the target, and then never improving. Because faster rockets score higher here, lazy detours get punished and the population keeps evolving cleaner, more direct paths.

* **Rockets stop when they arrive:** Once a rocket touches the target, it freezes in place. Its job is done, no need to keep flying.

---

## How It Works (step by step)

Each rocket has a brain (its `DNA`): a list of 300 small pushes that steer it, one per frame.

1. **Fly:** All rockets fly for up to 300 frames using their DNA (or stop early if they hit the target).
2. **Score:** Every rocket gets a fitness score based on how close it got and how fast it was.
3. **Pick parents:** Rockets are picked to be parents. Higher score = better odds of being picked.
4. **New generation:** Two parents' DNA is cut at a random point and glued together to make a child.
5. **Mutation:** Each move in the child's DNA has a 1% chance to mutate into something random.
6. **Repeat:** The new generation launches, and the whole cycle starts again, a little smarter each time.

---

## Prerequisites

Make sure you have Python and `pygame` installed:

```bash
pip install pygame
```

## Run it

```bash
python rockets.py
```
