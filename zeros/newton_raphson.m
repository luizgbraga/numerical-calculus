format compact;

disp(newtonRaphson(@f, @dfdx, 2, 0.01, 100));

function root = newtonRaphson(f, dfdx, x, tol, max_iter)
    i = 0;
    xi = x;

    while(abs(f(xi)) > tol || i > max_iter)
        next_x = xi - f(xi)/dfdx(xi);
        xi = next_x;
    end
    
    root = xi;
end

function y = f(x)
    y = x + cos(x);
end

function y_prime = dfdx(x)
    y_prime = 1 - sin(x);
end


