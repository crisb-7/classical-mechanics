function pos = posicion(a0,g,L) %Recibe el �ngulo, la aceleracion (g), la longitud y la velocidad tangencial
    a0 = deg2rad(a0); %Grados a radianes
    t = 0:0.1:15; %Vector de tiempo con las mismas dimensiones
    w = sqrt(g/L); %velocidad angular
    pos(1) = a0; %el vector de la posici�n se inicializa con el angulo inicial
    for i=2:length(t) %ciclo for con la f�rmula del p�ndulo para crear el vector completo de posici�n
    pos(i) = a0*cos(w*t(i));
    end
end