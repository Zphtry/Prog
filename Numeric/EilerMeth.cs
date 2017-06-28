<Eiler_1Order>
double dy(double x, double y)//y'=f(x,y)
void main()
{
	const int n;
	double x0, y0;
	double h;
	vector<double> X(n), Y(n);
	X[0] = x0;
	Y[0] = y0;
	for (int i = 0; i < n - 1; i++)
	{
		X[i + 1] = X[i] + h;
		Y[i + 1] = Y[i] + h * dy(X[i], Y[i]);
	}
}
</Eiler_1Order>
<Eiler_2Order>
double d2y(double x, double y, double dy)
void main()
{
	double x0, y0, dy0;
	double h;
	const int n;
	vector<double> X(n), Y(n), dY(n);
	X[0] = x0;
	Y[0] = y0;
	dY[0] = dy0;
	Y[1] = Y[0] + h * dY[0];
	for (int i = 0; i < n-2; ++i)
	{
		X[i + 1] = X[i] + h;
		Y[i + 2] = Y[i + 1] + h*(dY[i] + h*d2y(X[i], Y[i], dY[i]));
		dY[i + 1] = dY[i] + h * d2y(X[i], Y[i], dY[i]);
	}
}
</Eiler_2Order>
