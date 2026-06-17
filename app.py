from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <body class="bg-black text-white font-sans p-6" dir="rtl">
        <div class="max-w-xl mx-auto bg-gray-900 border border-blue-500 rounded-3xl p-8 shadow-2xl">
            <h1 class="text-3xl font-bold text-center text-blue-500 mb-6">Ahvmex Agency 🚀</h1>
            <p class="text-center text-gray-400 mb-8">للحصول على نسختك المجانية، املأ طلبك أدناه وسنتواصل معك فوراً للتنفيذ.</p>
            
            <div class="space-y-4">
                <input id="type" placeholder="نوع موقعك (مثال: متجر، شركة)" class="w-full p-4 rounded-xl bg-gray-800 border border-gray-700">
                <textarea id="desc" placeholder="اشرح لنا مواصفات موقعك..." class="w-full p-4 rounded-xl bg-gray-800 border border-gray-700 h-32"></textarea>
                <button onclick="send()" class="w-full bg-blue-600 hover:bg-blue-500 p-4 rounded-xl font-bold transition">إرسال الطلب (مجاناً)</button>
            </div>
        </div>

        <script>
            function send() {
                const t = document.getElementById('type').value;
                const d = document.getElementById('desc').value;
                const msg = `أهلاً Ahvmex، أريد موقعاً من نوع: ${t}. المواصفات: ${d}. هل يمكننا البدء؟`;
                window.open(`https://wa.me/212600000000?text=${encodeURIComponent(msg)}`, '_blank');
            }
        </script>
    </body>
    """
