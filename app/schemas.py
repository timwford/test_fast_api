from models import TestModel
from tortoise.contrib.pydantic import pydantic_model_creator

TestSchema = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}Schema")
TestSchemaCreate = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}SchemaCreate",
                                          exclude_readonly=True)
