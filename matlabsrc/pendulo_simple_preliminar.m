%Carpeta de archivos .m para simular el movimiento de un p�ndulo simple
%Se solicita al usuario introducir �nicamente el valor de la aceleracion
%gravitacional, la longitud del brazo del p�ndulo y el �ngulo inicial
L = input("Ingresa la longitud del p�ndulo \n"); 
a0 = input("Ingresa el �ngulo inicial \n");
g = input("Ingresa el valor de la aceleraci�n gravitacional \n");

%Velocidad tangencial = 0 debido a la naturaleza del p�ndulo simple

theta = posicion(a0,g,L);
velocidad = fvel(a0,g,L);
Euler = integracion(a0,g,L);
%Se llaman las funciones y se asignan a las variables
%int_num se refiere al vector con los valores de Y en la gr�fica de
%posicion con respecto al tiempo obtenidos mediante el m�todo de Euler
%(an�lisis num�rico)
t = 0:0.1:15; %vector de tiempo
O = [0 0]; %vector para el origen de la gr�fica para el pivote

%---------------------- P�ndulo Animado --------------------------------
grid on;
title('Movimiento de un P�ndulo'); 
xlabel('x');
ylabel('y');
%Simulaci�n del p�ndulo
for i=1:length(theta) 
   punto = L*[sin(theta(i)) -cos(theta(i))]; %Vector con las coordenadas X y Y
   bob = plot(punto(1),punto(2),'Marker','o','MarkerSize',10,'MarkerFaceColor','k'); %El marcador 
   %para la masa del p�ndulo
   pendulo = line([punto(1) O(1)],[punto(2) O(2)], 'Color','black'); %Se grafica una l�nea como
   %brazo del p�ndulo, uniendo el origen con los dos puntos respectivos
   xlim([-L-L*0.25 L+L*0.25])
   ylim([-L-L*0.25 L+L*0.25]) %Los l�mites de los ejes
   pause(0.1) %Pausa mezclado con el for para animar
   delete(pendulo) 
   delete(bob) %Se borra la l�nea y el marcador para que se grafique el siguiente punto
end

%---------------- Gr�ficas de Movimiento Animadas -------------------------

figure("Name", "Gr�ficas de movimiento")
%---------Posicion---------
subplot(2,1,1)
title('Posicion (\theta) con respecto al tiempo')
xlabel('t(s)')
ylabel('\theta (rads)')
axis([0 max(t) -max(theta) max(theta)]) 
hold on
comet(t, theta)
%------Posicion exacta mediante m�todos de an�lisis num�rico---------
Euler_anim = animatedline ('Color','b','LineWidth',1);
for i=1:length(t) % Ciclo for que se ejecuta una vez para cada valor de x.
 addpoints(Euler_anim,t(i),Euler(i)); % Agregar punto a la l�nea animada
 drawnow
 pause(0.1) % Detener ejecuci�n moment�neamente
end

%------Velocidad------
subplot(2,1,2)
hold off
title("Velocidad \theta' con respecto al tiempo")
xlabel('t(s)')
ylabel("\theta' (rad/s)")
axis([0 max(t) -max(velocidad) max(velocidad)])
hold on
comet(t, velocidad)



