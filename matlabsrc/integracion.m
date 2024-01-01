function int = integracion(a0,g,L) %Método de integración por análisis numérico
a0 = deg2rad(a0);
t = 0:0.1:15;
dt = 0.1;
w(1) = 0;
theta(1) = a0;
for i=1:length(t)-1 %Método de Euler-Cromer para calcular la posición estimada
    w(i+1) = w(i)-(g/L)*theta(i)*dt;
    theta(i+1) = theta(i)+w(i+1)*dt;
end
int = theta;
end