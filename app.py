from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-900 text-white flex items-center justify-center h-screen">
        <div class="text-center p-10 bg-gray-800 rounded-3xl shadow-2xl border border-gray-700">
            <h1 class="text-4xl font-bold text-blue-500 mb-4">Ahvmex Agency</h1>
            <p class="mb-6 text-gray-300">أهلاً بك! نحن هنا لنحول فكرتك إلى موقع احترافي.</p>
            <a href="https://wa.me/212600000000" class="bg-blue-600 px-8 py-3 rounded-full font-bold hover:bg-blue-500 transition">تواصل معنا عبر واتساب</a>
        </div>
    </body>
    </html>
    """
