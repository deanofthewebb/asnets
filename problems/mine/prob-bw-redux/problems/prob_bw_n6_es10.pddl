(define (problem prob_bw_6_n6_es10_r610)
  (:domain prob_bw)
  (:objects b1 b2 b3 b4 b5 b6 - block)
  (:init (emptyhand) (on b1 b6) (on-table b2) (on b3 b2) (on b4 b5) (on b5 b1) (on-table b6) (clear b3) (clear b4))
  (:goal (and (emptyhand) (on-table b1) (on-table b2) (on b3 b4) (on b4 b1) (on b5 b2) (on b6 b5) (clear b3) (clear b6)))
)
