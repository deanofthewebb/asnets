(define (problem prob_bw_4_n4_es10_r410)
  (:domain prob_bw)
  (:objects b1 b2 b3 b4 - block)
  (:init (emptyhand) (on b1 b4) (on b2 b3) (on b3 b1) (on-table b4) (clear b2))
  (:goal (and (emptyhand) (on-table b1) (on b2 b1) (on-table b3) (on b4 b2) (clear b3) (clear b4)))
)
