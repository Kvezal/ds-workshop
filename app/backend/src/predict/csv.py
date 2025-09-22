from fastapi import APIRouter, Request, UploadFile, File, HTTPException
import io
from fastapi.responses import StreamingResponse

from model import CSVReader

predict_csv_router = APIRouter()

@predict_csv_router.post("/csv", summary='Предсказание по файлу')
def predict_csv(request: Request, file: UploadFile):
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise HTTPException(503, "Model is not ready")

    csv = CSVReader(file)
    df = model.predict_from_df(csv.df)

    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=data.csv"}
    )
