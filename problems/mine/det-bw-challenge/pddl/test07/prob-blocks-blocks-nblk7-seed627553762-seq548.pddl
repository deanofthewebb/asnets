(define (problem blocks-nblk7-seed627553762-seq548)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b2) (on b2 b6) (on b3 b5) (on b4 b1) (on b5 b4) (on b6 b7) (ontable b7) (clear b3))
    (:goal (and (handempty) (ontable b1) (on b2 b7) (on b3 b4) (on b4 b5) (on b5 b2) (on b6 b1) (ontable b7) (clear b3) (clear b6))))
