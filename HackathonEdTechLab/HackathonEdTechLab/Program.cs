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

        public static List<Character> ReadFile(string fileName)
        {
            using (var csv = new CsvReader(File.OpenText(fileName)))
            {
                csv.Configuration.IgnoreBlankLines = true;
                csv.Configuration.IsHeaderCaseSensitive = false;

                var result = csv.GetRecords<Character>().ToList();
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

        public static void WriteFile(string fileName, List<Data> listData)
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

        public static List<Data> CreateData(List<Character> listFeature)
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
