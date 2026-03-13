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
        //System.Collections.Generic.List<AITool>(tools) // AIClient requires an IList<AITool>
