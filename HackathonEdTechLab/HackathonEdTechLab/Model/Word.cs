using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackathonEdTechLab.Model
{
    class Word
    {
        private List<Character> value;

        public Word()
        {
            value = new List<Character>();
        }

        public void appendChar(Character c)
        {
            value.Add(c);
        }
        
        public string ToString()
        {
            return new string(value.Select(c => (char)c.KeyCode).ToArray());
        }

        public int Count()
        {
            return value.Count;
        }

        public void Clear()
        {
            value.Clear();
        }
    }
}
