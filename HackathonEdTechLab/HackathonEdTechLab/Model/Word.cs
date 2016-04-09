using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackathonEdTechLab.Model
{
    class Word
    {
        public List<Character> value { get; set; }

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
            return new string(value.Select(c => (char)c.KeyCode).ToArray()).ToUpper();
        }

        public int Count()
        {
            return value.Count;
        }

        public void Clear()
        {
            value.Clear();
        }

        public Int64 Duration()
        {
            if (value.Count == 0)
            {
                return 0;
            }

            if (value.Count == 1)
            {
                return value[0].KeyUp - value[0].KeyDown;
            }

            Character first = value[0];
            Character last = value[value.Count - 1];
            return last.KeyUp - first.KeyDown;
        }
    }
}
