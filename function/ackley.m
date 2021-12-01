function [out]=ackley(in)
x=in;
e=exp(1);
out = (20 + e-20*exp(-0.2*sqrt((1/2).*sum(x.^2,2)))-exp((1/2).*sum(cos(2*pi*x),2)));
end