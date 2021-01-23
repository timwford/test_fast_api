import uvicorn
from fastapi import FastAPI, HTTPException

from tortoise.contrib.fastapi import register_tortoise

from database import TORTOISE_ORM
from models import TestModel
from enums import Test
from schemas import TestSchema, TestSchemaCreate

app = FastAPI()

register_tortoise(app, config=TORTOISE_ORM)


@app.get("/")
async def root():
    return {"welcome": "http://127.0.0.1:5000/docs"}


@app.get("/test/{id}")
async def get_test_by_id_(id: int):
    test = TestModel.filter(id=id).first()
    results = await TestSchema.from_queryset_single(test)

    return results


@app.get("/test", response_model=list[TestSchema])
async def get_all_tests():
    all_moods = TestModel.all()
    results = await TestSchema.from_queryset(all_moods)

    return results


@app.post("/test", status_code=201)
async def make_new_test(new_test: TestSchemaCreate):
    """
    valid, msg = validate(new_mood)

    if not valid:
        return HTTPException(status_code=422, detail=msg)
    """

    new_mood_model = TestModel(**new_test.__dict__)
    await new_mood_model.save()

    return new_test


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080, log_level="info")
