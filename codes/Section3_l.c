#include <stdio.h>
#include <stdlib.h>

int main ()
{
double x[6] = {1.0,2.0,3.0,4.0,2.0,1.0}, y[20];
int k = 20;

for(int i = 0; i < k; i++)
    y[i] = 0.0;

y[0] = x[0];
y[1] = -0.5*y[0]+x[1];

for (int i = 2; i < k-1; i++)
{
	if (i < 6)
		y[i] = -0.5*y[i-1]+x[i]+x[i-2];
	else if (i > 5 && i < 8)
		y[i] = -0.5*y[i-1]+x[i-2];
	else
		y[i] = -0.5*y[i-1];
}

FILE *xn = fopen ("/home/rahhul_17/Documents/LSP/filter/files/xn.txt", "w");
if (xn == NULL)
{
    printf ("Error opening file!\n");
	exit (0);
}
for (int i  = 0; i < 6; i++)
    fprintf (xn, "%lf\n", x[i]);
fclose (xn);

FILE *yn = fopen ("/home/rahhul_17/Documents/LSP/filter/files/yn.txt", "w");
if (yn == NULL)
{
    printf ("Error opening file!\n");
	exit (0);
}
for (int i  = 0; i < k; i++)
    fprintf (yn, "%lf\n", y[i]);
fclose (yn);

return 0;
}

