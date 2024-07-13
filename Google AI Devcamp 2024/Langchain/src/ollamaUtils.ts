import { Ollama } from "langchain/llms/ollama";

// model must be the same that is running in ollama
export const model = new Ollama({
    baseUrl: 'http://localhost:11434',
    model: 'gemma:2b'
  });

export const isRunning = () => {

  // todo: call ollama ping/health endpoin
  return true;
}