module Tools.ToolsBase

open Microsoft.Extensions.AI
open System.Reflection
open System.ComponentModel

type ToolsBase() =
    abstract GetTools: unit -> AITool seq // System.Collections.Generic.IList<AITool> 
    default this.GetTools() = 
        let tools = 
            this.GetType().GetMethods(BindingFlags.Public ||| BindingFlags.Instance)
            |> Seq.choose (fun m ->
                // Only pick methods that have a Description attribute
                let attr = m.GetCustomAttribute<DescriptionAttribute>()
                if isNull attr then None
                else
                    // Create the AIFunction and upcast to AITool
                    Some (AIFunctionFactory.Create(m, this) :> AITool)
        )
        tools

/// Convert a sequence os AITool sequence to a List that is required for the Agent contructor
let asList (tools:AITool seq seq) =
    let finalSeq = tools |> Seq.fold (fun state tools -> Seq.append state tools) Seq.empty<AITool>
    System.Collections.Generic.List<AITool>(finalSeq)