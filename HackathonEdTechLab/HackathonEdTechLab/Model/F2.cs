using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackathonEdTechLab.Model
{
    class F2
    {
        public string value { get; set; }
        public List<Int64> listDuration { get; set; }

        public F2()
        {
            listDuration = new List<Int64>();
        }

        public double Avegare()
        {
            double sum = listDuration.Sum();

            return listDuration.Count == 0 ? 0 : sum / listDuration.Count;
        }
    }
}
