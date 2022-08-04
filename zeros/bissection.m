format compact;

% deve ser contínua em [a, b] 
% f(a) * f(b) < 0 => deve haver uma raiz
% objetivo: diminuir a amplitude desse intervalo [a, b] até um episolon

disp(rootBissect(@f, -10, 10, 0.1));

function [x, err] = rootBissect(fn, xMin, xMax, tol)
    a = xMin;
    b = xMax;
    err = b - a;
    while err > tol
        x = (b + a)/2;
        if fn(x) * fn(a) > 0
            a = x;
        else 
            b = x;
        end
        err = b - a;
    end
end

function y = f(x)
    y = cos(x) + x;
end
