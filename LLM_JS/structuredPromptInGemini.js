// node --version # Should be >= 18
// npm install @google/generative-ai

const {
  GoogleGenerativeAI,
  HarmCategory,
  HarmBlockThreshold,
} = require("@google/generative-ai");

const MODEL_NAME = "gemini-1.5-pro-latest";
const API_KEY = "YOUR_API_KEY";

async function run() {
  const genAI = new GoogleGenerativeAI(API_KEY);
  const model = genAI.getGenerativeModel({ model: MODEL_NAME });

  const generationConfig = {
    temperature: 1,
    topK: 0,
    topP: 0.95,
    maxOutputTokens: 8192,
  };

  const safetySettings = [
    {
      category: HarmCategory.HARM_CATEGORY_HARASSMENT,
      threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
      category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
      threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
      category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
      threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
      category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
      threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
  ];

  const parts = [
    {text: "You are a product marketer targeting a Gen Z audience. Create exciting and\nfresh advertising copy for products and their simple description. Keep copy\nunder a few sentences long."},
    {text: "Product: 復古球鞋"},
    {text: "Product Copy: 讓我們一起接場吧！有了"},
    {text: "Product: 超柔軟連帽上衣"},
    {text: "Product Copy: 迎接全新的男女通用連帽衫，同時保持舒適與時尚！這款連帽衫採用 100% 純棉製成，既柔軟又舒適，整天佩戴也很舒適。即使在最寒冷的日子中，只要運用半刷而來的溫度就能保暖。"},
    {text: "Product: 時尚大衣"},
    {text: "Product Copy: "},
  ];

  const result = await model.generateContent({
    contents: [{ role: "user", parts }],
    generationConfig,
    safetySettings,
  });

  const response = result.response;
  console.log(response.text());
}

run();