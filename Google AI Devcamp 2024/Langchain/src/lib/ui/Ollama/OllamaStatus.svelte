<script lang="ts">
    import Icon from "@iconify/svelte";
    import { model, isRunning } from "../../../ollamaUtils";

    export let isDefined: boolean = !!model
    export let isReady = isDefined && isRunning();
</script>

{#if isDefined}
    <span class="text-bold">{model.model} 
        {#if isReady} 
        <Icon
            icon="fluent:checkmark-24-filled"
            color="green"
            width="24"
            height="24" 
            class="mx-auto inline" />
        {:else}
        <Icon
            icon="fluent:error-circle-24-filled"
            color="red"
            width="24"
            height="24" 
            class="mx-auto inline" />
        {/if}
    </span>
{:else}
<span style="color: red">
    Ollama model not defined
</span>
{/if}
