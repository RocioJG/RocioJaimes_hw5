#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main(void){
FILE *Rocio, *Rocio1;
/*Cargo datos iniciales y creo archivo para guardar resultados*/
Rocio=fopen("canal_ionico.txt", "r");
Rocio1=fopen("canal_ionico1.txt", "r");

int i, j, cont, cont1;
cont=0;
cont1=0;
float *x, *y, *x1, *y1;
/*Variables observadas de grafica generada en python. Son iguales para las dos*/
float x_obs, y_obs, r_obs, alpha, betha, x_obs1, y_obs1, r_obs1, rmax, xmax, ymax;
x_obs= 3.0;
y_obs= 5.0;
r_obs= 2.0;

rmax= 5.0;
xmax= 10.0;
ymax= 10.0;

x_obs1= 2.2;
y_obs1= 5.0;
r_obs1= 2.0;
/*Cuanto va a variar*/
float var=1.5;
float var_rad=2.5;
/*Declaro variables random*/
float randr, randx, randy, randr1, randx1, randy1;
/*variables que van a quedar entre 0 y 1*/
float rr, rx, ry, rr1, rx1, ry1;
/*variables van a quedar entre -0.5 y 0.5*/
float rr5, rx5, ry5, rr51, rx51, ry51;
/*random nuevas*/
float r_new, x_new, y_new, r_new1, x_new1, y_new1;
/*tamanho de x y y. Mismo para los dos archivos de texto*/
x=malloc(42*sizeof(float));
y=malloc(42*sizeof(float));

x1=malloc(42*sizeof(float));
y1=malloc(42*sizeof(float));

/*leo los archivos*/
for( i=0; i<42; i++){
	fscanf(Rocio, "%f %f\n", &x[i], &y[i]);
/*	printf("x= %f\n", x[i]);
	printf("y= %f\n", y[i]);*/
}
for( i=0; i<42; i++){
	fscanf(Rocio1, "%f %f\n", &x1[i], &y1[i]);
}

/*MCMC */
for(i=0; i<50000; i++)
{
/*Creo numeros random  necesito que se muevan en la varianza*/	
	randr=drand48();	
	randx=drand48();
	randy=drand48();

	randr1=drand48();	
	randx1=drand48();
	randy1=drand48();

/*convierto los random entre -1 y 1*/
	rr= 1-(2*randr);
	rx= 1-(2*randx);
	ry= 1-(2*randy);

	rr1= 1-(2*randr1);
	rx1= 1-(2*randx1);
	ry1= 1-(2*randy1);

/*-varianza a +varianza*/
	rr5= rr*var_rad;
	rx5= rx*var;
	ry5= ry*var;

	rr51= rr1*var_rad;
	rx51= rx1*var;
	ry51= ry1*var;

/*nuevo r va a ser el observado de las graficas de python + el numero entre varianza positiva y negativa*/
	r_new=r_obs+rr5;
	x_new= x_obs+rx5;
	y_new=y_obs+ry5;
	
	r_new1=r_obs1+rr51;
	x_new1=x_obs1+rx51;
	y_new1=y_obs1+ry51;

	for (j=0; j<42; j++)
	{
		if(pow((r_new+1),2)== (pow((x_new-x[j]),2)+pow((y_new-y[j]),2)))
		{
			cont++;
		}

	}

	for (j=0; j<42; j++)
	{
		if(pow((r_new1+1),2)== (pow((x_new1-x1[j]),2)+pow((y_new1-y1[j]),2)))
		{
			cont1++;
		}

	}

/*ciclos para archivo 0*/
	if(cont==0 && r_new<rmax && x_new<xmax && y_new<ymax)
	{
		alpha= r_new/r_obs;
		if(alpha >1.0)
		{
			r_obs=r_new;
			x_obs=x_new;
			y_obs=y_new;
		}	
		else
		{
			betha= drand48();
			if(betha<alpha)
			{
				r_obs=r_new;
				x_obs=x_new;
				y_obs=y_new;
			}
			else
			{
				r_obs= r_obs;
				x_obs= x_obs;
				y_obs=y_obs;
			}
		}
	}
	else
	{
		r_obs= r_obs;
		x_obs= x_obs;
		y_obs=y_obs;
	}
/*Ciclos para archivo 1*/
	if(cont1==0 && r_new<rmax && x_new<xmax && y_new<ymax)
	{
		alpha= r_new1/r_obs1;
		if(alpha >1.0)
		{
			r_obs1=r_new1;
			x_obs1=x_new1;
			y_obs1=y_new1;
		}	
		else
		{
			betha= drand48();
			if(betha<alpha)
			{
				r_obs1=r_new1;
				x_obs1=x_new1;
				y_obs1=y_new1;
			}
			else
			{
				r_obs1=r_obs1;
				x_obs1=x_obs1;
				y_obs1=y_obs1;
			}
		}
	}
	else
	{
		r_obs1=r_obs1;
		x_obs1=x_obs1;
		y_obs1=y_obs1;
	}

	printf("%f %f %f %f %f %f\n ", x_obs, y_obs, r_obs, x_obs1, y_obs1, r_obs1);

}
}
