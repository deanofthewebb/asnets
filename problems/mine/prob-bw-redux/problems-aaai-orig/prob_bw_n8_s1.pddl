(define (problem prob_bw_8_n8_s1)
  (:domain prob_bw)
  (:objects b1 b2 b3 b4 b5 b6 b7 b8 - block)
  (:init (emptyhand) (on b1 b2) (on-table b2) (on-table b3) (on b4 b7) (on b5 b8) (on b6 b4) (on b7 b1) (on-table b8) (clear b3) (clear b5) (clear b6))
  (:goal (and (emptyhand) (on-table b1) (on b2 b8) (on-table b3) (on-table b4) (on b5 b7) (on-table b6) (on b7 b1) (on b8 b5) (clear b2) (clear b3) (clear b4) (clear b6)))
)