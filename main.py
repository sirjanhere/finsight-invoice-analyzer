from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io

app = FastAPI(title="FinSight Invoice Analyzer")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        pdf_stream = io.BytesIO(contents)
        total_sum = 0.0

        with pdfplumber.open(pdf_stream) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    # First row assumed to be headers
                    headers = [h.strip() for h in table[0] if h]
                    if "Total" not in headers:
                        continue
                    total_idx = headers.index("Total")
                    item_idx = headers.index("Item") if "Item" in headers else 0

                    for row in table[1:]:
                        if not row or len(row) <= total_idx:
                            continue
                        item = str(row[item_idx]).strip() if row[item_idx] else ""
                        if "Thingamajig" in item:
                            try:
                                val = str(row[total_idx]).replace(",", "").strip()
                                total_sum += float(val)
                            except:
                                pass
        return {"sum": round(total_sum, 2)}

    except Exception as e:
        return {"error": str(e)}
