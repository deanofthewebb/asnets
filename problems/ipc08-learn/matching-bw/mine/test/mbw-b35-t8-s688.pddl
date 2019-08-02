

(define (problem mbw-b35-t8-s688)
(:domain matching-bw-typed)
(:requirements :typing)
(:objects h1 h2 - hand b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 b26 b27 b28 b29 b30 b31 b32 b33 b34 b35  - block)
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
 (on b2 b30)
 (solid b3)
 (block-positive b3)
 (on b3 b31)
 (solid b4)
 (block-positive b4)
 (on b4 b1)
 (solid b5)
 (block-positive b5)
 (on b5 b15)
 (solid b6)
 (block-positive b6)
 (on b6 b4)
 (solid b7)
 (block-positive b7)
 (on-table b7)
 (solid b8)
 (block-positive b8)
 (on b8 b23)
 (solid b9)
 (block-positive b9)
 (on b9 b7)
 (solid b10)
 (block-positive b10)
 (on b10 b17)
 (solid b11)
 (block-positive b11)
 (on-table b11)
 (solid b12)
 (block-positive b12)
 (on-table b12)
 (solid b13)
 (block-positive b13)
 (on b13 b29)
 (solid b14)
 (block-positive b14)
 (on b14 b18)
 (solid b15)
 (block-positive b15)
 (on b15 b20)
 (solid b16)
 (block-positive b16)
 (on b16 b24)
 (solid b17)
 (block-positive b17)
 (on b17 b27)
 (solid b18)
 (block-negative b18)
 (on b18 b35)
 (solid b19)
 (block-negative b19)
 (on b19 b10)
 (solid b20)
 (block-negative b20)
 (on b20 b19)
 (solid b21)
 (block-negative b21)
 (on b21 b26)
 (solid b22)
 (block-negative b22)
 (on b22 b2)
 (solid b23)
 (block-negative b23)
 (on b23 b21)
 (solid b24)
 (block-negative b24)
 (on b24 b6)
 (solid b25)
 (block-negative b25)
 (on b25 b32)
 (solid b26)
 (block-negative b26)
 (on-table b26)
 (solid b27)
 (block-negative b27)
 (on b27 b25)
 (solid b28)
 (block-negative b28)
 (on-table b28)
 (solid b29)
 (block-negative b29)
 (on b29 b11)
 (solid b30)
 (block-negative b30)
 (on b30 b5)
 (solid b31)
 (block-negative b31)
 (on b31 b9)
 (solid b32)
 (block-negative b32)
 (on-table b32)
 (solid b33)
 (block-negative b33)
 (on-table b33)
 (solid b34)
 (block-negative b34)
 (on b34 b12)
 (solid b35)
 (block-negative b35)
 (on b35 b3)
 (clear b8)
 (clear b13)
 (clear b14)
 (clear b16)
 (clear b22)
 (clear b28)
 (clear b33)
 (clear b34)
)
(:goal
(and
 (on b1 b8)
 (on b2 b20)
 (on b4 b23)
 (on b5 b12)
 (on b6 b13)
 (on b7 b26)
 (on b8 b15)
 (on b9 b22)
 (on b10 b21)
 (on b11 b3)
 (on b12 b24)
 (on b13 b1)
 (on b14 b35)
 (on b15 b14)
 (on b17 b10)
 (on b18 b6)
 (on b19 b11)
 (on b22 b28)
 (on b24 b18)
 (on b25 b29)
 (on b27 b25)
 (on b28 b17)
 (on b30 b2)
 (on b32 b34)
 (on b33 b7)
 (on b34 b31)
 (on b35 b9))
)
)

