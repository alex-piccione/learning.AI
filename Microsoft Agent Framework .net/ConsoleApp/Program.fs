open System.Reflection
open System.Threading
open Microsoft.Extensions.Configuration
open Helper
open Library
open Spectre.Console

let config =
    ConfigurationBuilder()
        .AddUserSecrets(Assembly.GetExecutingAssembly()) // assembly is required to give the runtime the correct one where to fiuind the UserSecretsId
        //.AddAzureKeyVault(Uri("https://your-vault.vault.azure.net/"), DefaultAzureCredential())
        .Build()

let key = config.Require "OpenAI:API_KEY"

let openai_models = [
    "gpt-4o",
    "gpt-4.1-mini",
    "gpt-5",
    "gpt-5-mini"
    ]

let agent = WeatherAgent.CreateChatClientUsingOpenAI(key, "gpt-4o")

let question = AnsiConsole.Ask<string>("[bold green]Ask the agent about the weather:[/]")

let response = agent.Ask(question, CancellationToken.None) |> Async.RunSynchronously

AnsiConsole.MarkupLine($"[yellow]{response}[/]")

()