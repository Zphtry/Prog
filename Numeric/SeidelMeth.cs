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
