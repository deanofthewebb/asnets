(define (problem blocks-nblk7-seed627553762-seq899)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b6) (on b2 b3) (ontable b3) (on b4 b7) (ontable b5) (on b6 b4) (on b7 b5) (clear b1) (clear b2))
    (:goal (and (handempty) (on b1 b7) (on b2 b5) (ontable b3) (ontable b4) (ontable b5) (on b6 b1) (on b7 b3) (clear b2) (clear b4) (clear b6))))