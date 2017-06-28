<Gauss>
int m;
vector<vector<double>> A(m, vector<double>(m));//левая часть(коэфф. при иксах)
vector<double> F(m);//правая часть(свободные члены)
//прямой ход
for (int i = 0; i < m - 1; ++i)//проход по подматрицам
	for (int j = i + 1; j < m; ++j)//по строкам
	{
		double coeff = -A[i][i] / A[j][i];
		F[j] *= coeff;
		F[j] += F[i];
		for (int k = i; k < m; ++k)//по столбцам
		{
			A[j][k] *= coeff;
			A[j][k] += A[i][k];
		}
	}

//обратный ход
vector<double> X(m);
for (int i = m - 1; i >= 0; --i)
{
	X[i] = F[i] / A[i][i];
	for (int j = i + 1; j < m; ++j)
		X[i] -= X[j] * A[i][j] / A[i][i];
}
</Gauss>

<Seidel>
bool converge(int m, vector<double> X, vector<double> P, double eps)//Функция, определяющая близки ли X и P с точностью eps
{
	double norm = 0;
	for (int i = 0; i < m; i++) norm += (X[i] - P[i])*(X[i] - P[i]);
	if (sqrt(norm) >= eps)	return false;
	return true;
}
void main()
{
	int m;//Размерность матрицы A
	double eps;//Точность решения
	vector<vector<double>> A(m, vector<double>(m));//левая часть(коэффициенты при иксах)
	vector<double> F(m);//правая часть(свободные члены)
	vector<double> X(m), P(m);//Текущее решение(X) и предыдущее(P)
        A = Transp(A) * A; //Обе части уравнения нужно умножить на A транспонированную
        F = Transp(A) * F;
	do
	{
		for (int i = 0; i < m; ++i) P[i] = X[i];//Запоминаем иксы в P
		for (int i = 0; i < m; ++i)
		{
			X[i] = F[i];
			for (int j = 0; j < m; ++j)
				if (j != i) X[i] -= A[i][j] * X[j];
			X[i] /= A[i][i];
		}
	} while (!converge(m, X, P, eps));
}
</Seidel>

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
