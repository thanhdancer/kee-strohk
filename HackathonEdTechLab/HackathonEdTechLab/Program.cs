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
        static void Main(string[] args)
        {
            string fileName = "";
            if (args == null || args.Length < 1)
            {
                // throw new ArgumentNullException("args");
                fileName = "haidt4.txt";
            }
            else
            {
                fileName = args[0];
            }

            var listFeature = ReadFile(fileName);
            var listData = CreateData(listFeature);

            // write list of words
            var listWords = CreateWords(listFeature);
            WriteWords("words.txt", listWords);
            WriteFile("Vector.txt", listData);

            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }

        public static List<Feature> ReadFile(string fileName)
        {
            using (var csv = new CsvReader(File.OpenText(fileName)))
            {
                csv.Configuration.IgnoreBlankLines = true;
                csv.Configuration.IsHeaderCaseSensitive = false;

                var result = csv.GetRecords<Feature>().ToList();
                return result;
            }
        }

        public static List<string> CreateWords(List<Feature> listFeature)
        {
            List<string> result = new List<string>();
            StringBuilder sb = new StringBuilder("");
            for (int index = 0; index < listFeature.Count; index++)
            {
                // alphabet character
                if ((listFeature[index].KeyCode >= (int)'a' && listFeature[index].KeyCode <= (int)'z') ||
                    (listFeature[index].KeyCode >= (int)'A' && listFeature[index].KeyCode <= (int)'Z'))
                {
                    sb.Append((char)listFeature[index].KeyCode);
                }
                // not alphabet
                else
                {
                    if (sb.Length > 0)
                    {
                        result.Add(sb.ToString());
                    }
                    sb.Clear();
                }
            }
            return result;
        }

        public static void WriteFile(string fileName, List<Data> listData)
        {
            var csv = new CsvWriter(File.CreateText(fileName));
            csv.Configuration.SkipEmptyRecords = true;
            csv.Configuration.QuoteAllFields = false;
            csv.Configuration.HasHeaderRecord = false;
            csv.WriteRecords(listData);
        }

        public static void WriteWords(string fileName, List<string> listWord)
        {
            File.WriteAllLines(fileName, listWord);
        }

        public static List<Data> CreateData(List<Feature> listFeature)
        {
            List<Data> listData = new List<Data>();

            for (int index = 0; index < listFeature.Count; index++)
            {
                var data = new Data
                {
                    CharCode = listFeature[index].KeyCode,
                    F1 = listFeature[index].KeyUp - listFeature[index].KeyDown,
                    F2 = index == listFeature.Count - 1 ? 0 : (listFeature[index + 1].KeyDown - listFeature[index].KeyUp),
                    F3 = index == listFeature.Count - 1 ? 0 : (listFeature[index + 1].KeyDown - listFeature[index].KeyDown),
                    F4 = 0
                };

                listData.Add(data);
            }
            return listData;
        }
    }
}
