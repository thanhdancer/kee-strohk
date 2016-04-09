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
            if (args == null || args.Length == 0)
            {
                // throw new ArgumentNullException("args");
            }

            string fileName = "haidt4.txt";

            var listFeature = ReadFile(fileName);



            var listData = CreateData(listFeature);
            //WriteFile("test.txt", listData);
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

        //public static List<string> CreateWords(List<Feature> listFeature)
        //{

        //}

        public static void WriteFile(string fileName, List<Data> listData)
        {
            var csv = new CsvWriter(File.CreateText(fileName));
            csv.Configuration.SkipEmptyRecords = true;
            csv.Configuration.QuoteAllFields = false;
            csv.Configuration.HasHeaderRecord = false;
            csv.WriteRecords(listData);
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
