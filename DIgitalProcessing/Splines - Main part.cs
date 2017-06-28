using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Splines
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }



        double a()
        {
            if (radioButton1.Checked)
                return 0;

            if (radioButton2.Checked)
                return -1;

            if (radioButton3.Checked)
                return 1;

            return 0;
        }

        double b()
        {
            if (radioButton1.Checked)
                return 1;

            if (radioButton2.Checked)
                return 1;

            if (radioButton3.Checked)
                return 3;

            return 0;
        }

        double h_real, h_inter;

        Draw draw;

        double Z()
        {
            if (radioButton1.Checked)
                return 170;

            if (radioButton2.Checked)
                return 150;

            if (radioButton3.Checked)
                return 7;

            return 0;
        }




        private void MainForm_Load(object sender, EventArgs e)
        {
            draw = new Draw(pictureBox1);

            h_real = 0.1;

            h_inter = 0.5;

        }



        double RealF(double x)
        {
            if (radioButton1.Checked)
                return Math.Exp(-x);

            if (radioButton2.Checked)
                return Math.Sin(Math.PI * x);

            if (radioButton3.Checked)
                return x * Math.Log(x) + Math.Exp(x);

            return 0;
        }



        void DrawReal()
        {
            int N = (int)((b() - a()) / h_real) + 1;

            double[] X = new double[N];

            double[] Y = new double[N];

            for (int i = 0; i < N; i++)
            {
                X[i] = a() + i * h_real;

                Y[i] = RealF(X[i]);
            }


            draw.DisplayArr(X, Y, Color.Green, Z());
            
        }

        void DrawInterpolate()
        {
            int N = (int)((b() - a()) / h_inter) + 1;

            double[] X = new double[N];

            double[] Y = new double[N];

            for (int i = 0; i < N; i++)
            {
                X[i] = a() + i * h_inter;

                Y[i] = RealF(X[i]);
            }



            Matrix matrix = new Matrix(X, Y);

            N = (int)((b() - a()) / h_real) + 1;

            X = new double[N];

            Y = new double[N];

            for (int i = 0; i < N; i++)
            {
                X[i] = a() + i * h_real;

                Y[i] = matrix.Interpolate(X[i]);
            }

            draw.DisplayArr(X, Y, Color.Red, Z());

        }

        void All()
        {
            draw.Clear();

            DrawReal();

            DrawInterpolate();
        }



        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            All();
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            All();
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            All();
        }
    }
}

