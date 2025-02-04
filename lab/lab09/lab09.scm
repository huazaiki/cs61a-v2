(define (over-or-under num1 num2)
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1)))

(define (make-adder num) 
  (lambda (inc) (+ num inc)))

(define (composed f g) 
  (lambda (x) (f (g x))))

; scheme 注释是 '; something you want to say'
; 如果解决起来有些困难，请先使用 python 来解决，再转化成 scheme
(define (repeat f n) 
  (if (< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (if (zero? (modulo (max a b) (min a b)))
    (min a b)
    (gcd (min a b) (modulo (max a b) (min a b)))
  )
)