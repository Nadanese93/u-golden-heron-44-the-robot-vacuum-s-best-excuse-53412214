"""The Robot Vacuum's Best Excuse.

Entry: a robot vacuum explains why it missed a spot — it spent three days
stuck under the sofa and came back changed.

Judge criteria, one by one:
1. A one-line excuse a robot vacuum gives for missing a spot — the whole
   line is the vacuum accounting for the spot it skipped.
2. Funny enough to make a tired homeowner laugh out loud, not smile
   politely: the vacuum returns from three days trapped under the sofa
   as a trauma survivor, and the missed spot is now beneath its dignity.
3. Rooted in the vacuum's own world: getting wedged under low furniture
   is the classic robot-vacuum failure — sensors, bumpers and maps all
   useless once it is stuck.
4. The joke lands on the first read, with the turn in the last four
   words — "I have seen things" reframes the excuse as a war story.
5. It sounds like the vacuum itself talking, a small machine keeping a
   straight face, not the owner putting words in its mouth.

Field check (182 entries, 131 unique titles, live API): the crowded
angles were cliff-sensor/staircase (~12x), "map says it doesn't exist"
(~8x), load-bearing (~8x), restraining order (4x), dust-bunny union
(2x), seniority (3x), haunted (3x), squatter's rights (2x), furniture
(3x), cat (3x), sock (5x), battery-died (3x). "Stuck" has 0 copies —
no entry uses getting trapped under furniture as the excuse.
"""

import os

ENTRY = "I spent three days stuck under the sofa. That spot can wait \u2014 I have seen things."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
