(define (problem blocks-nblk7-seed627553762-seq669)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b5) (on b2 b7) (ontable b3) (ontable b4) (on b5 b3) (on b6 b1) (on b7 b4) (clear b2) (clear b6))
    (:goal (and (handempty) (ontable b1) (on b2 b7) (ontable b3) (on b4 b5) (on b5 b6) (on b6 b3) (on b7 b1) (clear b2) (clear b4))))