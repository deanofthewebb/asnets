(define (problem blocks-nblk7-seed627553762-seq301)
    (:domain blocks)
    (:objects b1 b2 b3 b4 b5 b6 b7 - block)
    (:init (handempty) (ontable b1) (on b2 b4) (on b3 b5) (ontable b4) (on b5 b1) (ontable b6) (on b7 b3) (clear b2) (clear b6) (clear b7))
    (:goal (and (handempty) (on b1 b5) (ontable b2) (ontable b3) (on b4 b1) (on b5 b2) (ontable b6) (on b7 b3) (clear b4) (clear b6) (clear b7))))
