from fastapi import APIRouter, HTTPException

from app.utils.set100 import First100NaturalNumbers
from app.utils.schemas import MissingRequest, MissingResponse

router = APIRouter()


@router.post("/missing", response_model=MissingResponse, tags=["stateless"])
def compute_missing(payload: MissingRequest):
    """
    ### Extracts a number from the set 1..100 and calculates the missing number without maintaining state.
    """
    try:
        s = First100NaturalNumbers()
        s.Extract(payload.number)
        missing = s.missing_number()

        return MissingResponse(
            extracted=payload.number,
            missing=missing,
            message=f"The extracted number was {payload.number} and the calculated missing number is {missing}.",
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal error while calculating the missing number.",
        )
