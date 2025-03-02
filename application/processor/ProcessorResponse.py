import dataclasses


@dataclasses.dataclass
class ResponseBodyCard:
    id: str
    card_code: str
    exp_month: str
    exp_year: str
    type: str | bool  # visa
    valid: bool


@dataclasses.dataclass
class ResponseBody:
    amount: int
    approved: bool
    failure_code: int | str
    failure_message: str | str
    id: str
    card: ResponseBodyCard


@dataclasses.dataclass
class ProcessorResponse:
    body: ResponseBody
