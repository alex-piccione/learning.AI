import { json, type RequestHandler } from '@sveltejs/kit';
import { RunnableSequence } from 'langchain/schema/runnable';
import { StringOutputParser } from 'langchain/schema/output_parser';
import { model } from '../../../ollamaUtils';

export const POST: RequestHandler = async ({ request }) => {
  const { question } = await request.json();

  const chain = RunnableSequence.from([model, new StringOutputParser()]);

  const response = await chain.invoke(question);

  return json(response);
};
