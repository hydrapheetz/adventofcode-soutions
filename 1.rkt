#lang racket
(define (stairs v)
    (cond
      [(string=? v "(") 1]
      [(string=? v ")") -1]
	  [else 0]
      ))

(define (consume-stairs s)
    (cond
     [(= (string-length s) 0) 0]
     [else (cons (stairs (substring s 0 1))
            (list (consume-stairs (substring s 1))))]))

(define (find-first-basement s floor-number a)
  (cond
	[(= floor-number -1) a]
	[else
		(find-first-basement (substring s 1) (+ floor-number (stairs (substring s 0 1))) (+ a 1))])) 

(define fartbutt (port->string (open-input-file "C:/users/hydrapheetz/documents/code/aoc/input.txt")))

(find-first-basement fartbutt 0 0)
(foldr (lambda (l r) (+ l r)) 0 (flatten (consume-stairs "))(((((")))
