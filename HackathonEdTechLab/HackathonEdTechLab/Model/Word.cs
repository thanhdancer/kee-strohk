using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackathonEdTechLab.Model
{
    class Word
    {
        private StringBuilder value;

        public Word()
        {
            value = new StringBuilder("");
        }

        public void appendChar(char c)
        {
            value.Append(c);
        }
        
        public string ToString()
        {
            return value.ToString();
        }

        public int Count()
        {
            return value.Length;
        }

        public void Clear()
        {
            value.Clear();
        }
    }
}
