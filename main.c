#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef	struct	s_city
{
	double	sej;
	double	che;
	double	gon;
	double	new_sej;
	double	new_che;
	double	new_gon;
	double	sej_ratio;
	double	che_ratio;
	double	gon_ratio;
}				t_city;

void	initialize(t_city *city)
{
	city->sej = 350000;
	city->che = 660000;
	city->gon = 110000;
}

int		main(void)
{
	t_city	*city;
	int		year;

	city = malloc(sizeof(t_city));

	initialize(city);
	year = 0;
	//while(city->sej + city->gon < 550000)
	while (year < 10000)
	{
		city->new_sej = city->sej * 0.92 + city->che * 0.01 + city->gon * 0.10 + 4800;
		city->new_che = city->che * 0.98 + city->sej * 0.05 + city->gon * 0.05;
		city->new_gon = city->che * 0.01 + city->sej * 0.03 + city->gon * 0.85;
		city->sej_ratio = (city->new_sej / city->sej) * 100;
		city->che_ratio = (city->new_che / city->che) * 100;
		city->gon_ratio = (city->new_gon / city->gon) * 100;
		city->sej = city->new_sej;
		city->che = city->new_che;
		city->gon = city->new_gon;
		printf("======year : %d======\n", year + 1);
		printf("city->sej : %lf, diff : %lf\n", city->sej, city->sej_ratio - 100);
		printf("city->che : %lf, diff : %lf\n", city->che, city->che_ratio - 100);
		printf("city->gon : %lf, diff : %lf\n", city->gon, city->gon_ratio - 100);
		year++;
	}
}
