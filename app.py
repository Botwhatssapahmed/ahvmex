from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <body class="bg-gray-950 text-white font-sans">
        <section class="text-center py-20 px-6">
            <h1 class="text-5xl font-bold text-blue-500 mb-6">Ahvmex Agency</h1>
            <p class="text-xl text-gray-400 mb-10">صمم موقعك الاحترافي اليوم. اختر باقتك، تواصل معنا، وابدأ رحلة النجاح.</p>
            <a href="#services" class="bg-blue-600 px-8 py-4 rounded-full font-bold hover:bg-blue-500 transition">شاهد خدماتنا</a>
        </section>

        <section id="services" class="max-w-4xl mx-auto p-6 grid md:grid-cols-2 gap-8">
            <div class="bg-gray-900 p-8 rounded-2xl border border-gray-700">
                <h2 class="text-2xl font-bold mb-4">التصميم الأولي (مجاناً)</h2>
                <p class="text-gray-400 mb-6">نقدم لك تصوراً أولياً لموقعك لتتأكد من جودتنا قبل أي التزام مالي.</p>
                <a href="https://wa.me/YOUR_PHONE_NUMBER" class="text-blue-400 font-bold underline">اطلب المعاينة الآن عبر واتساب</a>
            </div>
            
            <div class="bg-blue-900 p-8 rounded-2xl border border-blue-700">
                <h2 class="text-2xl font-bold mb-4">التنفيذ الكامل والدفع</h2>
                <p class="text-blue-200 mb-6">بعد الموافقة على المعاينة، تواصل معنا لتأكيد الدفع وسنقوم بإطلاق موقعك فوراً.</p>
                <a href="https://wa.me/YOUR_PHONE_NUMBER" class="bg-white text-blue-900 px-6 py-2 rounded-lg font-bold">تواصل للدفع والتنفيذ</a>
            </div>
        </section>
    </body>
    """
