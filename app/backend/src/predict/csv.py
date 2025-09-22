from fastapi import APIRouter, Request, UploadFile, HTTPException
import io
from fastapi.responses import StreamingResponse
from pandas import errors
from pathlib import Path

from model import CSVReader

predict_csv_router = APIRouter()

@predict_csv_router.post("/csv", summary='Предсказание по файлу')
def predict_csv(request: Request, file: UploadFile):
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise HTTPException(503, "Model is not ready")

    ext = Path(file.filename).suffix.lower()
    if ext != '.csv':
        raise HTTPException(status_code=400, detail="Неверное расширение. Ожидается CSV-файл")

    try:
        csv = CSVReader(file)
        df = model.predict_from_df(csv.df)
    except errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Загружен пустой CSV-файл")
    except errors.ParserError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка парсинга CSV: {e}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Неверный формат файла: {e}")

    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"}
    )
