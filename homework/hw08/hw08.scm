(define (ascending? s) 
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s)))))
            

(define (my-filter pred s) 
    (cond ((null? s) '())
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 
    (define (f lst1 lst2 turn)
        (cond ((null? lst1) lst2)
            ((null? lst2) lst1)
            ((= turn 1) (cons (car lst1) (f (cdr lst1) lst2 2)))
            ((= turn 2) (cons (car lst2) (f lst1 (cdr lst2) 1)))))
    (f lst1 lst2 1))

(define (no-repeats s) 
    (if (null? s)
        s
        (cons (car s)
            (no-repeats (filter (lambda (n) (not (= (car s) n))) (cdr s))))))