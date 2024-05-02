/**
 * 這是一個使用 Google Generative AI 進行對話的範例程式。
 * 執行: node chatBoxInGemini.js
 * conference: https://dev.to/devarshishimpi/how-to-create-an-ai-chatbot-with-google-gemini-using-nodejs-pn6
 */
import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";
// 用於在終端上輸出彩色文字
import chalk from 'chalk';
// 用於顯示進度條或繞圈等待的套件
import ora from 'ora';
// 用於獲取使用者輸入的套件
import prompt from 'prompt-sync';

import dotenv from 'dotenv';
dotenv.config();

const promptSync = prompt();

const MODEL_NAME = "gemini-1.5-pro-latest";
const API_KEY = process.env.GEMINI_API_KEY;

const GENERATION_CONFIG = {
  temperature: 1,
  topK: 0,
  topP: 0.95,
  maxOutputTokens: 8192,
};
const SAFETY_SETTINGS = [
  { category: HarmCategory.HARM_CATEGORY_HARASSMENT, threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE },
  { category: HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE },
  { category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE },
  { category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE },
];

// 用來保存聊天歷史紀錄的陣列
let chatHistory = [];
async function runChat() {
  // 顯示一個初始化中的進度條
  const spinner = ora('Initializing chat...').start();
  try {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
    // 開始聊天，初始化一個聊天對象
    const chat = model.startChat({
      generationConfig: GENERATION_CONFIG,
      safetySettings: SAFETY_SETTINGS,
      history: [],
    });
    // 停止進度條
    spinner.stop();

    // 進入無限迴圈，等待使用者輸入。如果使用者輸入 "exit"，則退出程式
    while (true) {
      const userInput = promptSync(chalk.green('You: '));
      if (userInput.toLowerCase() === 'exit') {
        console.log(chalk.gray('Chat history:'));
        console.log(chalk.gray(chatHistory.map(entry => `${entry.role}: ${entry.parts}`).join('\n')));
        console.log(chalk.yellow('Goodbye!'));
        // process.exit(0); 表示正常結束程式
        process.exit(0);
      }
      const result = await chat.sendMessage(userInput);
      if (result.error) {
        console.error(chalk.red('AI Error:'), result.error.message);
        continue;
      }
      const response = result.response.text();
      console.log(chalk.blue('AI:'), response);
      // console.log('AI result:', result)
      // console.log('AI result.response:', result.response)

      // 將使用者輸入和 AI 回覆加入到聊天歷史紀錄中
      chatHistory.push({ role: 'user', parts: [userInput] });
      chatHistory.push({ role: 'model', parts: [response] });
    }
  } catch (error) {
    spinner.stop();
    console.error(chalk.red('An error occurred:'), error.message);
    // process.exit(1) 表示程式發生了錯誤或者無法繼續執行
    process.exit(1);
  }
}

runChat();