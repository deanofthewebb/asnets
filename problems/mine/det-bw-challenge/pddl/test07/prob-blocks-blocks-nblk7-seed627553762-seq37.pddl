(define (problem blocks-nblk7-seed627553762-seq37)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b7) (ontable b2) (ontable b3) (on b4 b6) (on b5 b1) (on b6 b2) (ontable b7) (clear b3) (clear b4) (clear b5))
    (:goal (and (handempty) (ontable b1) (on b2 b5) (on b3 b1) (on b4 b3) (ontable b5) (on b6 b7) (on b7 b4) (clear b2) (clear b6))))