format compact;

disp(fixed_point(@f, @phi, -1, 0.0001, 30));

function root = fixed_point(f, phi, x0, tol, max_iter)
    k = 0;
    xi = x0;

    while abs(f(xi)) > tol && k < max_iter
        xi = phi(xi);
        k = k + 1;
    end
    root = xi;
end

function y = f(x)
    y = x^2 - exp(x);
end

function g = phi(x)
    g = (-1) * sqrt(exp(x));
end
