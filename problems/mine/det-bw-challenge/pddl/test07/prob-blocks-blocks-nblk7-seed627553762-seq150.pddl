(define (problem blocks-nblk7-seed627553762-seq150)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (ontable b1) (on b2 b3) (ontable b3) (on b4 b1) (on b5 b4) (on b6 b5) (ontable b7) (clear b2) (clear b6) (clear b7))
    (:goal (and (handempty) (on b1 b3) (on b2 b7) (on b3 b5) (ontable b4) (on b5 b4) (ontable b6) (on b7 b1) (clear b2) (clear b6))))