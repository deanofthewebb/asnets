(define (problem prob_bw_6_n6_es7_r607)
  (:domain prob_bw)
  (:objects b1 b2 b3 b4 b5 b6 - block)
  (:init (emptyhand) (on b1 b2) (on-table b2) (on b3 b4) (on-table b4) (on b5 b1) (on b6 b3) (clear b5) (clear b6))
  (:goal (and (emptyhand) (on-table b1) (on b2 b6) (on b3 b2) (on b4 b5) (on b5 b3) (on b6 b1) (clear b4)))
)
