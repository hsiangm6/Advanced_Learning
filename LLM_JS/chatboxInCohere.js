import { CohereClient } from 'cohere-ai';
import chalk from 'chalk';
import ora from 'ora';
import prompt from 'prompt-sync';
import dotenv from 'dotenv';

dotenv.config();

const promptSync = prompt();

const MODEL_NAME ="command";
const API_KEY = process.env.COHERE_API_KEY;
const GENERATION_CONFIG = {
  temperature: 0.9,
  topK: 1,
  topP: 1,
  maxOutputTokens: 2048,
};
let chatHistory = [];
async function runChat() {
  const spinner = ora('Initializing chat...').start();
  try {
    const genAI = new CohereClient({
      token: API_KEY,
    });

    spinner.stop();

    while (true) {
      const userInput = promptSync(chalk.green('You: '));
      if (userInput.toLowerCase() === 'exit') {
        console.log(chalk.yellow('Goodbye!'));
        process.exit(0);
      }
      const response = await genAI.chat({
        chatHistory: chatHistory,
        model: MODEL_NAME,
        message: userInput,
      });
      // let response = '';
      // for await (const message of chatStream) {
      //   if (message.eventType === 'text-generation') {
      //     response = response + message.text;
      //   }
      // }
      console.log(chalk.blue('AI:'), response.text);
      // 將使用者輸入和 AI 回覆加入到聊天歷史紀錄中
      chatHistory.push({ role: 'USER', message: userInput });
      chatHistory.push({ role: 'CHATBOT', message: response });
    }
  } catch (error) {
    spinner.stop();
    console.error(chalk.red('An error occurred:'), error.message);
    process.exit(1);
  }
}

runChat();