(define (problem blocks-nblk7-seed627553762-seq586)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b2) (on b2 b7) (ontable b3) (ontable b4) (on b5 b4) (on b6 b3) (ontable b7) (clear b1) (clear b5) (clear b6))
    (:goal (and (handempty) (ontable b1) (on b2 b5) (on b3 b6) (ontable b4) (on b5 b1) (ontable b6) (ontable b7) (clear b2) (clear b3) (clear b4) (clear b7))))
