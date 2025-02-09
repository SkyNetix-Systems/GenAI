<<<<<<< HEAD
const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const apiKey = process.env.GEMINI_API_KEY;
  const genAI = new GoogleGenerativeAI("AIzaSyBBNs8r-FOS1axeD51hTePVRL7I_qwCWbM");
  
  const model = genAI.getGenerativeModel({
    model: "gemini-2.0-flash-exp",
  });
  
  const generationConfig = {
    temperature: 1,
    topP: 0.95,
    topK: 40,
    maxOutputTokens: 8192,
    responseMimeType: "text/plain",
  };
  
    export async function runAI(prompt: string) {
      const chatSession = model.startChat({
        generationConfig,
        history: [
        ],
      });
    
      const result = await chatSession.sendMessage(prompt);
      return result.response.text();
    }
=======
>>>>>>> 0591152e7460dd07b3fb22375410a6ffc2df8b58

require('dotenv').config();

import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";

// Initialize API key and Generative AI instance
const apiKey = process.env.GEMINI_API_KEY!;
console.log("API Key:", process.env.GEMINI_API_KEY);  // Log the API key for debugging
const genAI = new GoogleGenerativeAI("AIzaSyDBTuqBgZ94yknNXnSOgNx79J233w9X5ZA");



// Define model and configuration
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash-exp",
});

const generationConfig = {
  temperature: 1,
  topP: 0.95,
  topK: 40,
  maxOutputTokens: 8192,
  responseMimeType: "text/plain",
};

// Function to run AI with a dynamic prompt
export async function runAI(prompt: string) {
  console.log(process.env.GEMINI_API_KEY);  // Check if it prints the correct key
  const chatSession = model.startChat({
    generationConfig,
    history: [],
  });

  const result = await chatSession.sendMessage(prompt); // Use dynamic prompt here
  return result.response.text();
}
