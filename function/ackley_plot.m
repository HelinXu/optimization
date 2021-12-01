x = -3:.01:3;
y = -3:.01:3;
[X,Y] = meshgrid(x,y);
in = [X(:), Y(:)];
out = ackley(in);
Z = reshape(out, size(X));
surf(X, Y, Z);
shading interp 
camlight
material dull