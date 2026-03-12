open System.Reflection
open System.Threading
open Microsoft.Extensions.Configuration
open Microsoft.Extensions.Logging
open Helper
open Agents.Wheater
open Spectre.Console
open Agents.Cryptocurrencies
open openAIClientBuilder

let ct = CancellationToken()

let logger = 
    Microsoft.Extensions.Logging.LoggerFactory.Create(
        fun builder -> builder.AddConsole() |> ignore
        ).CreateLogger("ConsoleApp")

let config =
    ConfigurationBuilder()
        .AddUserSecrets(Assembly.GetExecutingAssembly()) // assembly is required to give the runtime the correct one where to find the UserSecretsId
        //.AddAzureKeyVault(Uri("https://your-vault.vault.azure.net/"), DefaultAzureCredential())
        .Build()

let openAiKey = config.Get "OpenAI:API_KEY"

let openai_models = [
    "gpt-4o",
    "gpt-4.1-mini",
    "gpt-5",
    "gpt-5-mini"
    ]

let weather_model = "gpt-5"
let cryptocurrencies_model = "gpt-5-mini";

let wheatherAgent = WeatherAgent.CreateChatClientUsingOpenAI(logger, openAiKey, weather_model)

(*
//let question = AnsiConsole.Ask<string>("[bold green]Ask the agent about the weather:[/]")
//let question = "Dammi le coordinate geografiche di Pesaro"
let question = "Come è il tempo a Pesaro?"
AnsiConsole.MarkupLine($"[cyan]{question}[/]")
let response = wheatherAgent.Ask(question, CancellationToken.None) |> Async.RunSynchronously
AnsiConsole.MarkupLine($"[yellow]{response}[/]")
*)

let openAIClientBuilder = openAIClientBuilder.OpenAIClientBuilder(openAiKey)

let chatClient = OpenAIClientBuilder.BuildChatClient(openAiKey, cryptocurrencies_model)

let cryptocurrenciesAgent = CrytocurrenciesAgent(logger, chatClient, config.Get "Kraken:private key", config.Get "Kraken:public key")
let question = "What is my balance in Kraken?"
AnsiConsole.MarkupLine($"[cyan]{question}[/]")

task {
    let! response = cryptocurrenciesAgent.Ask(question, ct)
    AnsiConsole.MarkupLine($"[yellow]{response}[/]")
}
|> Async.AwaitTask
|> Async.RunSynchronously

()