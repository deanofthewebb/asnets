

(define (problem mbw-b09-t3-s1256)
(:domain matching-bw-typed)
(:requirements :typing)
(:objects h1 h2 - hand b1 b2 b3 b4 b5 b6 b7 b8 b9  - block)
(:init
 (empty h1)
 (empty h2)
 (hand-positive h1)
 (hand-negative h2)
 (solid b1)
 (block-positive b1)
 (on-table b1)
 (solid b2)
 (block-positive b2)
 (on-table b2)
 (solid b3)
 (block-positive b3)
 (on b3 b5)
 (solid b4)
 (block-positive b4)
 (on-table b4)
 (solid b5)
 (block-negative b5)
 (on b5 b9)
 (solid b6)
 (block-negative b6)
 (on b6 b1)
 (solid b7)
 (block-negative b7)
 (on b7 b2)
 (solid b8)
 (block-negative b8)
 (on b8 b4)
 (solid b9)
 (block-negative b9)
 (on b9 b7)
 (clear b3)
 (clear b6)
 (clear b8)
)
(:goal
(and
 (on b1 b8)
 (on b2 b9)
 (on b3 b6)
 (on b4 b7)
 (on b6 b4)
 (on b7 b5))
)
)


