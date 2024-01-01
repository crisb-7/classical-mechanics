function vel = fvel(a0,g,L) %Función que calcula la velocidad angular
    a0 = deg2rad(a0);
    t = 0:0.1:15;
    w = sqrt(g/L); %Velocidad angular
    for i=2:length(t) %Ciclo for que calcula los valores de omega para cada
        %valor del tiempo
    vel(i) = -a0*w*sin(w*t(i));
    end
end