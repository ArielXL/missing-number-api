from fastapi import APIRouter, HTTPException

from app.utils.set100 import First100NaturalNumbers
from app.utils.schemas import MissingRequest

router = APIRouter()


number_set = First100NaturalNumbers()


@router.post("/extract", tags=["stateful"])
def extract_number(payload: MissingRequest):
    """
    ### Extracts a number from the set 1..100 and updates the state.
    """
    try:
        number_set.Extract(payload.number)
        return {"message": f"Number {payload.number} extracted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/missing", tags=["stateful"])
def get_missing_number():
    """
    ### Gets the missing number from the set after an extraction.
    """
    if number_set.extracted is None:
        raise HTTPException(status_code=400, detail="No number has been extracted yet.")

    missing = number_set.missing_number()

    return {"extracted": number_set.extracted, "missing": missing}


@router.post("/reset", tags=["stateful"])
def reset_set():
    """
    ### Resets the set of numbers 1..100.
    """
    global number_set
    number_set = First100NaturalNumbers()
    return {"message": "The set has been reset."}
