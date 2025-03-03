# Author: Jack Hermanson
import dataclasses


@dataclasses.dataclass
class RequestCard:
    id: str
    name: str
    card_code: str
    exp_month: str
    exp_year: str
    currency: str


@dataclasses.dataclass
class RequestMerchantData:
    name: str
    network_id: str


@dataclasses.dataclass
class ProcessorRequest:
    id: str
    amount: int  # cents
    currency: str
    card: RequestCard
    merchant_data: RequestMerchantData
