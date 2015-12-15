#lang racket

(define problem-input (port->lines (open-input-file "C:/Users/hydrapheetz/documents/code/aoc/input_2.txt")))

(define (produce-measurement s)
    (map (lambda (x) (string->number x)) (string-split s "x")))

(define (paper-order measurements)
  (+ (* 2 (second measurements) (first measurements))
     (* 2 (first measurements) (third measurements))
     (* 2 (second measurements) (third measurements))
     (min (* (second measurements) (first measurements))
          (* (first measurements) (third measurements))
          (* (third measurements) (second measurements)))))


(paper-order '(2 3 4))

(foldr (lambda (l r) (+ l r)) 0 (map (lambda (x) (paper-order (produce-measurement x))) problem-input))
