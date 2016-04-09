using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using HackathonEdTechLab.Model;
using CsvHelper;

namespace HackathonEdTechLab
{
    class Program
    {
        const int number = 26;
        /*
        private static string[] commonChars = new string[] { "ng", "th", "ti", "on", "an", "he", "at", "er", "re",
                                                        "nd", "ha", "en", "to", "it", "ou", "ea", "hi", "is",
                                                        "or", "te", "ng", "nh", "th", "ai"};
        private static string[] commonWords = new string[] { "for", "and", "the", "is", "it", "you", "have", "of", "be",
                                                        "to", "that", "he", "she", "this", "they", "will", "i", "all",
                                                        "a", "him", "ta", "xa", "da", "cho"};
        */
        static void Main(string[] args)
        {
            string fileName = "";
            if (args == null || args.Length < 1)
            {
                // throw new ArgumentNullException("args");
                fileName = "hien.txt";
            }
            else
            {
                fileName = args[0];
            }

            var listChar = ReadFile(fileName);

            // write list of words
            var listWords = CreateWords(listChar);
            WriteWords("words.txt", listWords);
            CreateData(listChar, listWords);

            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        public static List<Character> ReadFile(string fileName)
        {
            using (var csv = new CsvReader(File.OpenText(fileName)))
            {
                csv.Configuration.IgnoreBlankLines = true;
                csv.Configuration.IsHeaderCaseSensitive = false;
                //csv.Configuration.IgnoreReadingExceptions = true;

                var result =new List<Character>();
                while (csv.Read())
                {
                    var record = csv.GetRecord<Character>();
                    result.Add(record);
                }
                return result;
            }
        }

        public static List<Word> CreateWords(List<Character> listFeature)
        {
            List<Word> result = new List<Word>();
            Word word = new Word();
            for (int index = 0; index < listFeature.Count; index++)
            {
                // alphabet character
                if ((listFeature[index].KeyCode >= (int)'a' && listFeature[index].KeyCode <= (int)'z') ||
                    (listFeature[index].KeyCode >= (int)'A' && listFeature[index].KeyCode <= (int)'Z'))
                {
                    word.appendChar(listFeature[index]);
                }
                // not alphabet
                else
                {
                    if (word.Count() > 0)
                    {
                        result.Add(word);
                    }
                    word = new Word();
                }
            }
            return result;
        }

        public static void WriteFile<T>(string fileName, List<T> listData)
        {
            var csv = new CsvWriter(File.CreateText(fileName));
            csv.Configuration.SkipEmptyRecords = true;
            csv.Configuration.QuoteAllFields = false;
            csv.Configuration.HasHeaderRecord = false;
            csv.WriteRecords(listData);
        }

        public static void WriteWords(string fileName, List<Word> listWord)
        {
            File.WriteAllLines(fileName, listWord.Select(c => c.ToString()));
        }

        public static void CreateData(List<Character> listChar, List<Word> listWord)
        {
            CalculateF1(listChar);
            calculateF23(listChar);
            calculateF4(listWord);
        }

        private static void calculateF23(List<Character> listChar)
        {
            List<string> commonChars = new List<string>();
            using (var csv = new CsvReader(File.OpenText("diagram.txt")))
            {
                csv.Configuration.IgnoreBlankLines = true;
                csv.Configuration.IsHeaderCaseSensitive = false;
                int count = 1;

                while (csv.Read() && count <= number)
                {
                    var record = csv.GetRecord<Frequency>();
                    commonChars.Add(record.Value);
                    count++;
                }
            }

            List<F2> listF2 = new List<F2>();
            List<F3> listF3 = new List<F3>();

            for (int index = 0; index < commonChars.Count; index++)
            {
                listF2.Add(new F2
                {
                    value = commonChars[index]
                });

                listF3.Add(new F3
                {
                    value = commonChars[index]
                });
            }

            for(int index = 0; index < listChar.Count - 1; index++)
            {
                StringBuilder sb = new StringBuilder("");
                sb.Append((char)listChar[index].KeyCode);
                sb.Append((char)listChar[index + 1].KeyCode);

                for(int i = 0; i < listF2.Count; i++) 
                {
                    if (listF2[i].value.ToUpper().Equals(sb.ToString().ToUpper()))
                    {
                        listF2[i].listDuration.Add(listChar[index + 1].KeyDown - listChar[index].KeyUp);
                        listF3[i].listDuration.Add(listChar[index + 1].KeyDown - listChar[index].KeyDown);
                    }
                }
            }

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"F2.txt"))
            {
                foreach (var item in listF2)
                {
                    file.WriteLine(item.value + "," + item.Avegare());
                }
            }

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"F3.txt"))
            {
                foreach (var item in listF3)
                {
                    file.WriteLine(item.value + "," + item.Avegare());
                }
            }
        }

        private static void calculateF4(List<Word> listWord)
        {
            List<string> commonWords = new List<string>();
            using (var csv = new CsvReader(File.OpenText("diagram.txt")))
            {
                csv.Configuration.IgnoreBlankLines = true;
                csv.Configuration.IsHeaderCaseSensitive = false;
                int count = 1;

                while (csv.Read() && count <= number)
                {
                    var record = csv.GetRecord<Frequency>();
                    commonWords.Add(record.Value);
                    count++;
                }
            }

            List<F4> list = new List<F4>();
            for (int index = 0; index < commonWords.Count; index++)
            {
                list.Add(new F4
                {
                    value = commonWords[index]
                });
            }

            foreach (var w in listWord)
            {
                foreach (var cw in list)
                {
                    if (cw.value.ToUpper().Equals(w.ToString()))
                    {
                        cw.listDuration.Add(w.Duration());
                    }
                }
            }

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"F4.txt"))
            {
                foreach (var item in list)
                {
                    file.WriteLine(item.value + "," + item.Avegare());
                }
            }
        }

        private static void CalculateF1(List<Character> listChar)
        {
            List<F1> list = new List<F1>();
            for (int index = (int)'a'; index <= (int)'z'; index++)
            {
                list.Add(new F1
                {
                    value = (char) index
                });
            }

            foreach (var c in listChar)
            {
                if((c.KeyCode >= (int)'a' && c.KeyCode <= (int)'z') ||
                    (c.KeyCode >= (int)'A' && c.KeyCode <= (int)'Z'))
                {
                    int index = c.KeyCode - (int)'a';
                    if (index < 0)
                    {
                        index = c.KeyCode - (int)'A';
                    }
                    list[index].listDuration.Add(c.KeyUp - c.KeyDown);
                }
            }

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"F1.txt"))
            {
                foreach (var item in list)
                {
                    file.WriteLine(item.value + "," + item.Avegare());
                }
            }
        }
    }
}
