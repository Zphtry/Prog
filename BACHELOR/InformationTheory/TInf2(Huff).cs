using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TInf2_Huff_
{
    public partial class Form1 : Form
    {        
        public Form1()
        {
            InitializeComponent();
        }

        struct Word
        {
            public double P;

            public int CodeLength;

            public int[] Nums;
        }

        int n;

        //Массив вероятностей(типа листы дерева)
        Word[] Leafs;

        

        private void button1_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox1.Text, out n))
            {
                FillLeafs();

                PrintLeafs();

                Calc();

                PrintCodes();
            }
        }

        void PrintLeafs()
        {
            label4.Text = "";

            for (int i = 0; i < Leafs.Length; i++)

                label4.Text += string.Format("{0}\n", Leafs[i].P.ToString());
        }

        void PrintCodes()
        {
            label5.Text = "";

            foreach (var x in Leafs)

                label5.Text += x.CodeLength + "\n";
           
        }


        void FillLeafs()
        {
            Leafs = new Word[n];

            Random Rnd = new Random();

            double sig = 0;

            for (int i = 0; i < n; i++)
            {

                if (i != n - 1)
                {
                    Leafs[i].P = Math.Round((1 + Rnd.Next(-50, 50) / 100f) / Leafs.Length, 2);

                    sig += Leafs[i].P;
                }

                else Leafs[i].P = Math.Round(1 - sig, 2);
            }

            Leafs = Leafs.OrderByDescending(q => q.P).ToArray();

            for (int i = 0; i < Leafs.Length; i++)
            {
                Leafs[i].Nums = new int[1];

                Leafs[i].Nums[0] = i;

                Leafs[i].CodeLength = 1;
            }
        }



        void Calc()
        {
            Word[] Leafs2 = new Word[Leafs.Length];

            Leafs.CopyTo(Leafs2, 0);

            Forward(Leafs2);

        }

        void Forward(Word[] InArr)
        {
            if (InArr.Length > 2)
            {

                Backward(InArr[InArr.Length - 1]);

                Backward(InArr[InArr.Length - 2]);


                InArr[InArr.Length - 2].P += InArr[InArr.Length - 1].P;

                InArr[InArr.Length - 2].Nums = InArr[InArr.Length - 2].Nums.Concat(InArr[InArr.Length - 1].Nums).ToArray();


                Word[] RetArr = new Word[InArr.Length - 1];

                Array.Copy(InArr, RetArr, InArr.Length - 1);


                RetArr = RetArr.OrderByDescending(q => q.P).ToArray();


                Forward(RetArr);
            }

            else return;
        }

        void Backward(Word Elm)
        {
           foreach(var x in Elm.Nums)

                Leafs[x].CodeLength++;

        }
    }
}
