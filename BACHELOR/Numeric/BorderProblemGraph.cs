using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BorderProblemGraph
{

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }

        double h, eps;
        double a, b;
        double xl, yl, xr, yr;
        int n;

        private void Form1_Load(object sender, EventArgs e)
        {

            //Дано
            h = 0.5; eps = 0.005;
            a = -1000; b = 1000;
            xl = 0; yl = 10; xr = 10; yr = 0;
            n = (int)((xr - xl) / h);

            //Prepare
            Graphics g;
            pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(pictureBox1.Image);

            //Axis
            g.DrawLine(Pens.Black, new Point(0, pictureBox1.Height / 2), new Point(pictureBox1.Width, pictureBox1.Height / 2));
            g.DrawLine(Pens.Black, new Point(pictureBox1.Width / 2, 0), new Point(pictureBox1.Width / 2, pictureBox1.Height));

            //Scales


            //Graphic
            double dyl = MDP();
            double[] Y = Eiler2Nd(dyl);
            for (int i = 0; i < n; i++)
            {
                g.FillRectangle(Brushes.Red, (int)(1.2 * (pictureBox1.Width / 2 + i)), (int)(10 * Y[i]), 1, 1);
            }

        }

        double d2y(double x, double y, double dy)
        {
            return -2 * dy - 4 * y;
        }

        double[] Eiler2Nd(double dyl)
        {
            double[] X = new double[n];
            double[] Y = new double[n];
            double[] dY = new double[n];
            X[0] = xl;
            Y[0] = yl;
            dY[0] = dyl;
            Y[1] = Y[0] + h * dY[0];
            for (int i = 0; i < n - 2; ++i)
            {
                X[i + 1] = X[i] + h;
                Y[i + 2] = Y[i + 1] + h * (dY[i] + h * d2y(X[i], Y[i], dY[i]));
                dY[i + 1] = dY[i] + h * d2y(X[i], Y[i], dY[i]);
            }
            return Y;
        }

        double Minimizing(double dyl)
        {
            return Eiler2Nd(dyl)[n - 1] - yr;
        }

        double MDP()
        {
            if (Minimizing(a) == 0) return a;
            if (Minimizing(b) == 0) return b;
            while (Math.Abs(a - b) > 2 * eps)
            {
                double m = (a + b) / 2;
                if (Minimizing(m) == 0) return m;
                if (Minimizing(a) * Minimizing(m) > 0) a = m;
                else b = m;
            }
            return (a + b) / 2;
        }
    }
}
