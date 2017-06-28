using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TInf1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int m, n;//Размеры матрицы вероятностей

        double[,] P;//Матрица вероятностей

        double[] x, y; //ансамбли x, y


        double Hx, Hy, H_xy, H_yx, H_XY;//Энтропии H(x) H(y) H(X|Y) H(Y|X) H(XY)

        double[,] MutInfMat; //Матрица взаимной информации(Mutual information - MutInfMat)

        double AverMutInf;//Средняя взаимная инф.



        private void button1_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox1.Text, out m) && int.TryParse(textBox2.Text, out n))
            {
                Hx = 0;

                Hy = 0;

                AverMutInf = 0;


                FillP();

                PrintDim(P, label3);


                FillAns();

                PrintDim(x, label8);

                PrintDim(y, label9);


                CalcMutInf();

                PrintDim(MutInfMat, label5);


                CalcAverMutInf();

                label7.Text = AverMutInf.ToString();


                CalcH();

                label14.Text = Hx.ToString();

                label15.Text = Hy.ToString();

                label18.Text = H_xy.ToString();

                label19.Text = H_yx.ToString();

                label21.Text = H_XY.ToString();
            }
        }



        //Печать массива в label
        void PrintDim(double[] Dim, Label TOut)
        {
            TOut.Text = "";

            for (int i = 0; i < Dim.GetLength(0); i++)

                TOut.Text += string.Format("{0} ", Dim[i].ToString("0.00"));
        }

        //Печать матрицы в label
        void PrintDim(double[,] Dim, Label TOut)
        {
            TOut.Text = "";

            for (int i = 0; i < Dim.GetLength(0); i++)
            {
                for (int j = 0; j < Dim.GetLength(1); j++)

                    TOut.Text += string.Format("{0} ", Dim[i, j].ToString("0.00"));

                TOut.Text += '\n';
            }
        }



        //Заполнение матрицы вероятностей
        void FillP()
        {
            P = new double[m, n];

            Random Rnd = new Random();

            double sig = 0;

            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i != m - 1 || j != n - 1)
                    {
                        P[i, j] = Math.Round((1 + Rnd.Next(-50, 50) / 100f) / P.LongLength, 2);

                        sig += P[i, j];
                    }

                    else P[i, j] = Math.Round(1 - sig, 2);
                }
            }
        }

        //Заполнение ансамблей x и y
        void FillAns()
        {
            x = new double[m];

            y = new double[n];

            for (int i = 0; i < m; i++)

                for (int j = 0; j < n; j++)
                {
                    x[i] += P[i, j];

                    y[j] += P[i, j];
                }

        }



        //Вычисление взаимной инф.
        void CalcMutInf()
        {
            MutInfMat = new double[m, n];

            double sum1, sum2;

            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    sum1 = 0; sum2 = 0;

                    for (int k = 0; k < m; k++) sum1 += P[k, j];

                    for (int l = 0; l < n; l++) sum2 += P[i, l];

                    MutInfMat[i, j] = Math.Log(P[i, j] / (sum1 * sum2), 2);
                }
            }
        }

        //Средней взаимной инф.
        void CalcAverMutInf()
        {
            for (int i = 0; i < m; i++)

                for (int j = 0; j < n; j++)

                    AverMutInf += P[i, j] * MutInfMat[i, j];

            AverMutInf = Math.Round(AverMutInf, 2);
        }

        //Энтропия
        void CalcH()
        {
            for (int i = 0; i < m; i++)

                Hx -= x[i] * Math.Log(x[i], 2);

            Hx = Math.Round(Hx, 2);

            for (int j = 0; j < n; j++)

                Hy -= y[j] * Math.Log(y[j], 2);

            Hy = Math.Round(Hy, 2);


            H_xy = Hx - AverMutInf;

            H_yx = Hy - AverMutInf;

            H_XY = Hx + Hy - AverMutInf;
        }
    }
}
