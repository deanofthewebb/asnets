

(define (problem mbw-b14-t3-s1818)
(:domain matching-bw-typed)
(:requirements :typing)
(:objects h1 h2 - hand b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14  - block)
(:init
 (empty h1)
 (empty h2)
 (hand-positive h1)
 (hand-negative h2)
 (solid b1)
 (block-positive b1)
 (on b1 b12)
 (solid b2)
 (block-positive b2)
 (on b2 b3)
 (solid b3)
 (block-positive b3)
 (on b3 b6)
 (solid b4)
 (block-positive b4)
 (on b4 b11)
 (solid b5)
 (block-positive b5)
 (on-table b5)
 (solid b6)
 (block-positive b6)
 (on b6 b13)
 (solid b7)
 (block-positive b7)
 (on b7 b9)
 (solid b8)
 (block-negative b8)
 (on b8 b1)
 (solid b9)
 (block-negative b9)
 (on b9 b14)
 (solid b10)
 (block-negative b10)
 (on-table b10)
 (solid b11)
 (block-negative b11)
 (on-table b11)
 (solid b12)
 (block-negative b12)
 (on b12 b5)
 (solid b13)
 (block-negative b13)
 (on b13 b8)
 (solid b14)
 (block-negative b14)
 (on b14 b2)
 (clear b4)
 (clear b7)
 (clear b10)
)
(:goal
(and
 (on b2 b13)
 (on b3 b11)
 (on b4 b1)
 (on b6 b14)
 (on b8 b2)
 (on b9 b8)
 (on b10 b4)
 (on b11 b7)
 (on b12 b10)
 (on b13 b3)
 (on b14 b5))
)
)


