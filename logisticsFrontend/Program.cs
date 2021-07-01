using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Net.Http.Headers;
using System.Text;

namespace logisticsFrontend
{
    class Program
    {
        static readonly HttpClient _client = new HttpClient();

        private static void Main(string[] args)
        {
            Console.WriteLine(
                    "Welcome to the logistics API console interface!\n" +
                    "Following bellow you will find instructions for how to use the terminal: \n" +
                    "\n" +
                    "S + a number, for an example S5 will sell an amount of products \n" +
                    "I + a number, for an example I5 will add an amount of products \n" +
                    "L + enter will simply show the actual amount of products aviable" +
                    "\n" +
                    "The console will always just simply show the response from the api it is connected to. \n" +
                    "\n" +
                    "You can always also press ENTER to exit!"
                    );

            while (true)
            {
                string str = Console.ReadLine();

                // If the string is null, empty or only contains white spaces,
                // break out of the loop.
                if (string.IsNullOrWhiteSpace(str))
                {
                    Console.Write("OK. You pressed Enter. See you again! :)");
                    break;
                }
                var res = DecideHttpMethod(str);
                Console.WriteLine(GetStringFromTaskResult(res));
            };
        }

        // should be refactored to instead use baseurl instead. but the demands on the 
        //input towards the console makes it a bit tough to work with
        // we could always also add validation for the input in here so we have it in 
        //both the api and in the console. that would minimize corrupt api calls from 
        //users misusing the application.
        private static async Task<string> DecideHttpMethod(string input)
        {
            (string substringFirstCharacter, string substrinRestOfCharacters) = SlashString(input, 1);
            string caseString = substringFirstCharacter.ToUpper();
            switch (caseString)
            {
                case "S":
                    return await ExecuteMethod(
                        "http://localhost:5000/api/v1/sales",
                        "PATCH",
                        content: CreatePayload(substrinRestOfCharacters));
                case "I":
                    return await ExecuteMethod(
                        "http://localhost:5000/api/v1/delivery",
                        "PATCH",
                        content: CreatePayload(substrinRestOfCharacters));
                case "L":
                    return await ExecuteMethod("http://localhost:5000/api/v1/balance", "GET");
                default:
                    return "You did not begin the input with 'S', 'I' or 'L'";
            }
        }

        // this should probably be refactored to a kvp dict mapping structure instead using linq.
        private static Dictionary<string, object> CreatePayload (string input){
            return new Dictionary<string, object>()
            {
                {"balance_number", input}
            };
        }

        private static string GetStringFromTaskResult(Task<string> input)
        {
            if (!String.IsNullOrEmpty(input.Result))
            {
                return input.Result;
            }
            return "";
        }
        public static async Task<string> ExecuteMethod(string targetAbsoluteUrl, string methodName, List<KeyValuePair<string, string>> headers = null, Dictionary<string, object> content = null, string contentType = "application/json")
        {
            try
            {
                var httpMethod = new HttpMethod(methodName.ToUpper());
                _client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/json"));

                var requestMessage = new HttpRequestMessage(httpMethod, targetAbsoluteUrl);

                if (content != null || !string.IsNullOrWhiteSpace(contentType))
                {
                    var jsonDictionary = JsonConvert.SerializeObject(content);
                    requestMessage.Content = new StringContent(jsonDictionary, Encoding.UTF8, "application/json");
                }

                var response = await _client.SendAsync(requestMessage);

                return await response.Content.ReadAsStringAsync();
            }
            catch (Exception e)
            {
                return e.Message;
            }
        }
        
        static Tuple<string, string> SlashString(string fullString, int slashPos)
        {
            string leftString = "";
            string rightString = "";
            if (slashPos > 0 && fullString.Length >= 1)
            {
                leftString = fullString.Substring(0, slashPos);
                rightString = fullString.Substring(slashPos);
            }
            return Tuple.Create(leftString, rightString);
        }
    }
}
