(define (problem blocks-nblk7-seed627553762-seq492)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b3) (on b2 b1) (on b3 b7) (ontable b4) (on b5 b6) (on b6 b2) (on b7 b4) (clear b5))
    (:goal (and (handempty) (on b1 b4) (on b2 b7) (ontable b3) (ontable b4) (ontable b5) (on b6 b2) (on b7 b5) (clear b1) (clear b3) (clear b6))))