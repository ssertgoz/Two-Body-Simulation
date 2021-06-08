#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 4

struct TwoBodyModel{
	
	double m1; //mass1
	double m2;  //mass2
	double m12;  //mass1+mass2
	double u[N];  
	double position[N]; //position of body1 and body2
	
	
};

struct TwoBodyModel *m;


struct TwoBodyController{
	
	double T;
	double delT;
	double q;  //mass ratio
	double e;  //eccentiricity
	int method;
	
};

struct TwoBodyController *c; 

void init(struct TwoBodyModel *m,struct TwoBodyController *c){
	
	
	
	m->m1=1.0;
	m->m2=(c->q);
	m->m12=((m->m1)+(m->m2));
	m->position[0]=0;
	m->position[1]=0;
	m->position[2]=0;
	m->position[3]=0;
	m->u[0]=1;
	m->u[1]=0;
	m->u[2]=0;
	m->u[3]=(sqrt((1+(c->q))*(1+(c->e))));  //initial velocity n
	
}

double *derivative(struct TwoBodyModel *m,struct TwoBodyController *c){
	
	double *du;
	double *r,rr;
	int i;
	du=malloc(sizeof(double)*N);
	r=malloc(sizeof(double)*2);
	


	du[0]=0;
	du[1]=0;
	du[2]=0;
	du[3]=0;
	
    r[0]=(m->u[0]);
	r[1]=(m->u[1]);
	
	rr=(sqrt(pow(r[0],2)+pow(r[1],2)));  //distance between two bodies
	
	for(i=0;i<2;i++){
		du[i]=(m->u[i+2]);
		du[i+2]=-1*(((1+(c->q))*r[i])/ pow(rr,3));
		
		
	}
	
	free(r);
	return (du);
	
}

void rungekutta(struct TwoBodyModel *m,struct TwoBodyController *c){
	
	int i,j;
	double *du=malloc(sizeof(double)*N);
	
	double a[N]={((c->delT)/2.0),((c->delT)/2.0),c->delT,0};
	double b[N]={((c->delT)/6.0),((c->delT)/3.0),((c->delT)/3.0),((c->delT)/6.0)};
	double u0[N]={0,0,0,0};
	double ut[N]={0,0,0,0};
	
	for(i=0;i<N;i++){
		
		u0[i]=(m->u[i]);
		ut[i]=0;
	}
	
	
	for(j=0;j<N;j++){
		
		du=derivative(m,c);
		for(i=0;i<N;i++){
			m->u[i]=(u0[i]+a[j]*du[i]);
			ut[i]=(ut[i]+b[j]*du[i]);
			
		}
	}
	
	for(i=0;i<N;i++){
		
		m->u[i]=(u0[i]+ut[i]);
	}
	free(du);
	
}


void euler(struct TwoBodyModel *m,struct TwoBodyController *c){
	
	
	double *du=derivative(m,c);
	int i;
	for(i=0;i<4;i++){
		
		m->u[i]=((m->u[i])+((du[i])*(c->delT)));
		
	}
	
	free(du);
}

void calculatenewposition(struct TwoBodyModel *m){
	
	double r=1.0;
	double a1=((m->m2)/(m->m12))*r;
	double a2=((m->m1)/(m->m12))*r;
	m->position[0]=-a2*(m->u[0]);
	m->position[1]=-a2*(m->u[1]);
	m->position[2]=a1*(m->u[0]);
	m->position[3]=a1*(m->u[1]);
}


void App(struct TwoBodyModel *m,struct TwoBodyController *c){
	
	
	FILE *fptr;
	fptr=fopen("LocationVectorC.txt","w");
	int flag;
	int i;
	
	printf("Enter mass ratio(q):\n");
	scanf("%lf",&c->q);
	printf("Enter eccentricity(e):\n");
	scanf("%lf",&c->e);
	printf("Enter period(T):\n");
	scanf("%lf",&c->T);
	printf("Enter time step(deltaT):\n");
	scanf("%lf",&c->delT);
	printf("Choose a method:\n1-Runge Kutta\n2-Euler\n");
	scanf("%d",&c->method);
	
	init(m,c);
	
	for(i=0;i<((c->T)/(c->delT));i++){
		
		
		if(c->method==1){
			
			rungekutta(m,c);
			
		}
		else{
			euler(m,c);
		}
		
		calculatenewposition(m);
		fprintf(fptr,"%.17lf,",m->position[0]);
		fprintf(fptr,"%.17lf,",m->position[1]);
		fprintf(fptr,"%.17lf,",m->position[2]);
		fprintf(fptr,"%.17lf\n",m->position[3]);
		
		
	}
	
}

int main() {
	
	
	struct TwoBodyModel model;
	struct TwoBodyController control;
	App(&model,&control);
	
	
	
	return 0;
}
