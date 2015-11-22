using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Splines
{
    class Matrix
    {
        struct InterpolateNode
        {
            public double a, b, c, d, x;
        }


        double[,] M;

        double[] Alpha, Beta;

        InterpolateNode[] Result;

        int N;

        double[] X, Y;


        public Matrix(double[] X_in, double[] Y_in)
        {
            X = X_in; Y = Y_in;

            N = X_in.Length;

            M = new double[N, N];

            Alpha = new double[N];

            Beta = new double[N];

            Result = new InterpolateNode[N];

            CsCalc();

            OtherFieldsCalc();
        }


        void CsCalc()
        {
            Result[0].c = 0; Result[N - 1].c = 0;



            Alpha[0] = 0; Beta[0] = 0;


            double h_prev, h_next;

            double A, B, C, F, Z;

            for (int i = 1; i < N - 1; i++)
            {
                h_prev = X[i] - X[i - 1];

                h_next = X[i + 1] - X[i];


                A = h_prev;

                B = h_next;

                C = 2 * (h_prev + h_next);

                F = 6 * ((Y[i + 1] - Y[i]) / h_next - (Y[i] - Y[i - 1]) / h_prev);

                Z = A * Alpha[i - 1] + C;


                Alpha[i] = -B / Z;

                Beta[i] = (F - A * Beta[i - 1]) / Z;
            }



            for (int i = N - 2; i >= 0; --i)

                Result[i].c = Alpha[i] * Result[i + 1].c + Beta[i];
        }

        void OtherFieldsCalc()
        {

            for (int i = 0; i < N; i++)
            {
                Result[i].a = Y[i];

                Result[i].x = X[i];
            }


            double h_prev;

            for (int i = N - 1; i > 0; i--)
            {
                h_prev = X[i] - X[i - 1];

                Result[i].d = (Result[i].c - Result[i - 1].c) / h_prev;

                Result[i].b = h_prev * (2.0 * Result[i].c + Result[i - 1].c) / 6.0 + (Y[i] - Y[i - 1]) / h_prev;
            }
        }



        public double Interpolate(double x)
        {
            InterpolateNode thisNode;

            int i = 0; int j = N - 1;

            while (i + 1 < j)
            {
                int k = i + (j - i) / 2;

                if (x <= Result[k].x)
                    j = k;

                else
                    i = k;
            }

            thisNode = Result[j];

            double dx = x - thisNode.x;

            return thisNode.a + (thisNode.b + (thisNode.c / 2.0 + thisNode.d * dx / 6.0) * dx) * dx;

        }
    }
}
