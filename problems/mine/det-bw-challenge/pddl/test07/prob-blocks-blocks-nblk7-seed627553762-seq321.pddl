(define (problem blocks-nblk7-seed627553762-seq321)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (ontable b1) (on b2 b6) (on b3 b2) (on b4 b5) (on b5 b1) (ontable b6) (on b7 b4) (clear b3) (clear b7))
    (:goal (and (handempty) (on b1 b5) (ontable b2) (on b3 b4) (ontable b4) (on b5 b7) (on b6 b3) (on b7 b2) (clear b1) (clear b6))))
