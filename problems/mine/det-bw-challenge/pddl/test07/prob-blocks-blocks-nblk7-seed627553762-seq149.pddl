(define (problem blocks-nblk7-seed627553762-seq149)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (on b1 b2) (ontable b2) (on b3 b6) (on b4 b5) (on b5 b1) (ontable b6) (on b7 b3) (clear b4) (clear b7))
    (:goal (and (handempty) (on b1 b4) (on b2 b6) (ontable b3) (on b4 b3) (ontable b5) (ontable b6) (on b7 b5) (clear b1) (clear b2) (clear b7))))