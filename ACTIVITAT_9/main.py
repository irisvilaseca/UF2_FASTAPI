from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None

items_db = {
    1: {"name": "Item 1", "description": "First item", "price": 10.5, "tax": 1.0},
    2: {"name": "Item 2", "description": "Second item", "price": 20.0, "tax": 2.0},
}
@app.get("/items/")
async def read_items():
    return {"items": items_db}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        return {"error": f"Item with ID {item_id} not found."}
    return {"item_id": item_id, "item": item}


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items_db:
        deleted_item = items_db.pop(item_id)
        return {"message": "Item deleted successfully", "item": deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")