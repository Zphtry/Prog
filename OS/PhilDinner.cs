using System;
using System.Collections.Generic;
using System.Threading;

namespace PhilDinner
{
    public class Phil
    {
        bool isHunger;

        string name;

        int number;

        int waiting;

        public Phil(string name, int number)
        {
            this.name = name; this.number = number;
        }

        public void BeginDinner(object obj)
        {
            while (true)
            {
                Thread.Sleep(waiting);

                Switch();

                if (isHunger) GetFork((List<Fork>)obj);
            }
        }

        void GetFork(List<Fork> fork)
        {
            //Выбираем случайно время обеда философа

            waiting = new Random().Next(20 * System.DateTime.Now.Millisecond);

            //Вычисляем окружающие вилки

            int leftFork = number;

            int rightFork = (number + 1) % (fork.Count - 1);

            Console.WriteLine(name + " ждет вилку {0} или {1} ({2}мс)", leftFork, rightFork, waiting);


            //Если окружающие вилки свободны, занимаем обе, если нет -- ждём

            if (fork[leftFork].IsOccup || fork[rightFork].IsOccup) return;

            fork[leftFork].IsOccup = true;

            fork[rightFork].IsOccup = true;


            Console.WriteLine(name + " обедает ({0}мс)", waiting);

            Console.WriteLine("Вилки {0} и {1} заняты  ({2}мс)", leftFork + 1, rightFork + 1, waiting);

            Thread.Sleep(waiting);

            //Освобождаем вилки

            fork[leftFork].IsOccup = false;

            fork[rightFork].IsOccup = false;
        }

        void Switch()
        {
            isHunger = !isHunger;

            if (!isHunger) Console.WriteLine(name + " думает." + "\t ({0}мс)", waiting);
        }
    }

    public class Fork
    {
        public bool IsOccup;
    }

    class Program
    {
        static void Main()
        {
            //Списки вилок и философов
            List<Fork> Forks = new List<Fork>();

            List<Phil> Phils = new List<Phil>();

            int count = 5;

            for (var i = 0; i < count; i++)
            {
                Forks.Add(new Fork());

                Phils.Add(new Phil((i + 1).ToString(), i));

                new Thread(Phils[i].BeginDinner).Start(Forks);
            }
        }
    }
}
