/**
 * conference: https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct/discussions/3
 * @param data
 * @returns {Promise<any>}
 */
import dotenv from 'dotenv';
dotenv.config();
const API_KEY = process.env.HUGGINGFACE_API_KEY;
async function query(data) {
  const response = await fetch(
    "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-6.7b-instruct",
    {
      headers: { Authorization: `Bearer ${API_KEY}` },
      method: "POST",
      body: JSON.stringify(data),
    }
  );
  const result = await response.json();
  return result;
}

query({"inputs": "Can you please let us know more details about your "}).then((response) => {
  console.log(JSON.stringify(response));
});