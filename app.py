from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <link href="https://cdn.tailwindcss.com" rel="stylesheet">
    <body class="bg-black text-white p-6" dir="rtl">
        <div id="chatWindow" class="max-w-xl mx-auto bg-gray-900 border border-blue-500 rounded-3xl p-8 shadow-2xl">
            <h1 class="text-2xl font-bold text-blue-500 mb-4">Ahvmex Agency 🤖</h1>
            <div id="messages" class="h-64 overflow-y-auto bg-gray-800 p-4 rounded-xl mb-4 text-sm space-y-3">
                <p class="text-blue-300">مرحباً بك! أنا مساعد Ahvmex الذكي. اكتب نوع الموقع ومواصفاته وسأقوم بفتح طلب خاص لك.</p>
            </div>
            <div id="inputArea" class="flex gap-2">
                <input id="userMsg" class="flex-1 p-3 rounded-xl bg-gray-800 border border-gray-700" placeholder="اكتب هنا...">
                <button onclick="addMessage()" class="bg-blue-600 px-6 py-2 rounded-xl font-bold">إرسال</button>
            </div>
        </div>

        <script>
            function addMessage() {
                const input = document.getElementById('userMsg');
                const msgList = document.getElementById('messages');
                if(!input.value) return;

                // إضافة رسالة المستخدم
                msgList.innerHTML += `<p class='text-right text-white'>أنت: ${input.value}</p>`;
                
                // رسالة البوت
                msgList.innerHTML += `<p class='text-blue-300'>البوت: تم استلام طلبك للمعاينة! سيتم التواصل معك عبر هذا الموقع قريباً.</p>`;
                
                input.value = "";
                msgList.scrollTop = msgList.scrollHeight;
            }
        </script>
    </body>
    """
