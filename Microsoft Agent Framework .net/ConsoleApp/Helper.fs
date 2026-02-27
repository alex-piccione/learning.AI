module Helper

open Microsoft.Extensions.Configuration
open System.Runtime.CompilerServices

[<Extension>]
type ConfigurationRootExtensions =

    /// Gets required config value or fails with descriptive error.
    /// Usage: config.Require("mykey")
    [<Extension>]
    static member Require(this: IConfigurationRoot, key: string) : string =
        match this[key] with
        | null -> failwithf "Missing required config: %s" key
        | value -> value

    /// Gets required config value as 'T or fails.
    /// Usage: config.RequireAs<int>("Port")
    [<Extension>]
    static member RequireAs<'T>(this: IConfigurationRoot, key: string) : 'T =
        let value = this.Require(key)
        match System.Convert.ChangeType(value, typeof<'T>) with
        | (:? 'T as result) -> result
        | _ -> failwithf "Invalid config type for %s: expected %s" key (typeof<'T>.Name)