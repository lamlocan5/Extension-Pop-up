import os
import json
import requests
import asyncio
from typing import Dict, Any
from dotenv import load_dotenv

import nest_asyncio
nest_asyncio.apply()

# Tải biến môi trường từ file .env
load_dotenv()

class GeminiGrammarChecker:
    def __init__(self):
        """
        Khởi tạo Grammar Checker sử dụng API key từ biến môi trường
        """
        self.api_key = os.environ.get("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("Không tìm thấy GEMINI_API_KEY trong biến môi trường. Vui lòng thiết lập biến môi trường này.")
            
        # Cập nhật URL API với API Key đúng
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
    
    async def _call_gemini_api(self, prompt: str, response_format="json") -> Dict:
        """
        Gọi API Gemini với prompt đã được tạo
        
        Args:
            prompt: Prompt đã định dạng
            response_format: Định dạng phản hồi mong muốn (mặc định: json)
            
        Returns:
            Phản hồi từ API dưới dạng dictionary
        """
        headers = {
            "Content-Type": "application/json",
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.1,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 4096,
            }
        }
        
        # Chỉ định kiểu MIME khi yêu cầu JSON
        if response_format == "json":
            data["generationConfig"]["responseMimeType"] = "application/json"
        
        # Gửi request
        response = requests.post(
            self.api_url, 
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
        return response.json()
    
    async def check_grammar(self, text: str) -> Dict[str, Any]:
        """
        Kiểm tra lỗi ngữ pháp trong văn bản
        
        Args:
            text: Văn bản cần kiểm tra
            
        Returns:
            Dictionary chứa kết quả phân tích lỗi và văn bản đã sửa
        """
        # Cải thiện prompt để có kết quả tốt hơn
        prompt = f"""
        You are an expert English teacher analyzing a student's writing. Your task is to:

        1. Identify all grammar, spelling, and punctuation errors
        2. Provide a detailed explanation of each error
        3. Suggest corrections for each error
        4. Provide an improved version of the text
        5. All language is suggested in Vietnamese

        Return your analysis in the following JSON format only:
        {{
            "error_count": <number of errors>,
            "errors": [
                {{
                    "error_text": "<the text containing the error>",
                    "error_type": "<grammar/spelling/punctuation/word choice>",
                    "explanation": "<clear explanation of why it's incorrect>",
                    "correction": "<how to fix it correctly>"
                }},
                // Additional errors...
            ],
            "original_text": "<the original text>",
            "improved_text": "<the fully corrected text>"
        }}
        
        Here is the text to analyze:
        {text}
        """
        
        response = await self._call_gemini_api(prompt)
        
        # Trích xuất nội dung phản hồi từ API
        try:
            response_text = response["candidates"][0]["content"]["parts"][0]["text"]
            # Xử lý trường hợp khi phản hồi là chuỗi JSON
            if isinstance(response_text, str):
                # Tìm và trích xuất phần JSON từ phản hồi
                import re
                json_match = re.search(r'({.*})', response_text.replace('\n', ''), re.DOTALL)
                if json_match:
                    result = json.loads(json_match.group(1))
                else:
                    try:
                        result = json.loads(response_text)
                    except json.JSONDecodeError:
                        # Nếu không thể parse JSON, trả về kết quả đơn giản
                        return {"original_text": text, "improved_text": response_text, "error_analysis": "Could not parse detailed analysis"}
            else:
                result = response_text
            
            return result
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            # Xử lý lỗi và trả về kết quả đơn giản
            return {
                "original_text": text,
                "improved_text": text,
                "error_analysis": f"Error processing response: {str(e)}"
            }

# Chạy thử nghiệm
async def main():
    checker = GeminiGrammarChecker()
    
    sample_text = "Their are some common mistakes in this sentenses. Its importants to check you're grammar carefully."
    
    result = await checker.check_grammar(sample_text)
    
    print("Kết quả phân tích lỗi ngữ pháp:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    print("\nVăn bản gốc:")
    print(result.get("original_text", "Không có dữ liệu"))
    
    print("\nVăn bản sau khi sửa:")
    print(result.get("improved_text", "Không có dữ liệu"))
    print("Tổng số lỗi: ", result.get("error_count", "Không có dữ liệu"))
    if "errors" in result:
        print("\nChi tiết các lỗi:")
        for i, error in enumerate(result["errors"], 1):
            print(f"\nLỗi {i}:")
            print(f"- Đoạn văn bản lỗi: {error.get('error_text', 'N/A')}")
            print(f"- Loại lỗi: {error.get('error_type', 'N/A')}")
            print(f"- Giải thích: {error.get('explanation', 'N/A')}")
            print(f"- Cách sửa: {error.get('correction', 'N/A')}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
