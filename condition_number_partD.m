A = [   [15, -2, -3, -1, 0],
        [-2,-15, 0,  1, 3],
        [ 3, -9, 0,  2, 0],
        [ 1,  1, 2, -6, 2],
        [ 0,  3, 0,  2, -9]
       ];


Ainv = inv(A)

K = norm(A) * norm(Ainv)

if K <= 10^3
    display("The system is not ill-conditioned");
else
    display("System is ill-conditioned");
end
