using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Matrix_algorithm
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }



        double h;

        int N;

        double a, b, ya, yb;

        private void Form1_Load(object sender, EventArgs e)
        {
            a = 0; b = 1;

            ya = 0; yb = -1;

            N = 10;

            h = (b - a) / N;


            L = new double[N];

            K = new double[N];

            Y = new double[N + 1];

            Y[0] = ya; Y[N] = yb;


        }

        void Init()
        {
            L[0] = 0;

            K[1] = ya;

            if (radioButton1.Checked)
            {

            }

            if (radioButton2.Checked)
            {

            }

            if (radioButton3.Checked)
            {

            }


            double x;

            for (int i = 1; i < N; ++i)
            {
                x = a + h * i;

                L[i] = L_i(x, L[i - 1]);

                K[i] = K_i(x, K[i - 1], L[i - 1]);

            }

            for (int i = N - 1; i > 0; --i)
                Y[i] = L[i] * Y[i + 1] + K[i];
        }


        double alpha_i(double x)
        {
            return 0;
        }

        double beta_i(double x)
        {
            return -1;
        }

        double gamma_i(double x)
        {
            return 2 * x;
        }


        double a_i(double x)
        {
            return 2 - alpha_i(x) * h;
        }

        double b_i(double x)
        {
            return 2 * h * h * beta_i(x) - 4;
        }

        double c_i(double x)
        {
            return 2 + alpha_i(x) * h;
        }

        double f_i(double x)
        {
            return 2 * h * h * gamma_i(x);
        }


        double L_i(double x, double L_im1)
        {
            return -c_i(x) / (b_i(x) + a_i(x) * L_im1);
        }

        double K_i(double x, double K_im1, double L_im1)
        {
            return (f_i(x) - a_i(x) * K_im1) / (b_i(x) + a_i(x) * L_im1);
        }


        double[] L;

        double[] K;


        double[] Y;


        double ExactSolution(double x)
        {
            if (radioButton1.Checked)
                return Math.Sinh(x) / Math.Sinh(1) - 2 * x;
            return 0;
        }



        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            Init();

            double x;

            for (int i = 0; i < N + 1; ++i)
            {
                x = a + i * h;

                label1.Text +=  "\n" + x.ToString();

                label2.Text += "\n" + ExactSolution(x).ToString("F5");

                label3.Text += "\n" + Y[i].ToString("F5");
            }

        }
    }
}
