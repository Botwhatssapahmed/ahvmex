from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <body class="bg-gray-950 text-white flex justify-center items-center h-screen font-sans" dir="rtl">
        
        <div class="w-full max-w-md bg-gray-900 rounded-2xl shadow-2xl border border-gray-700 overflow-hidden relative">
            
            <div class="bg-blue-600 p-5 text-center shadow-md">
                <h2 class="text-2xl font-bold text-white">Ahvmex Bot 🤖</h2>
                <p class="text-sm text-blue-200 mt-1">متصل الآن - لإنشاء نسختك المجانية</p>
            </div>
            
            <div id="chatbox" class="h-96 overflow-y-auto p-5 space-y-4 bg-gray-800">
                <div class="bg-gray-700 p-4 rounded
