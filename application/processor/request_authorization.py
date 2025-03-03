# Author: Jack Hermanson
import json
from requests import post
from application import logger
from dataclasses import asdict

from application.processor.ProcessorRequest import ProcessorRequest
from application.processor.ProcessorResponse import ProcessorResponse, ResponseBody, ResponseBodyCard

PROCESSOR_BASE_URL = "https://us-central1-ict4310-275816.cloudfunctions.net/credit_card_validate"


def request_authorization(processor_request: ProcessorRequest):
    request_body = asdict(processor_request)
    logger.info(f"Making request to processor:\n{json.dumps(request_body, indent=2)}")
    response = post(
        url=f"{PROCESSOR_BASE_URL}/api/validate",
        headers={"Content-Type": "application/json"},
        json=request_body,
    )
    if response.ok:
        response_json = response.json()
        logger.info(f"Processor response:\n{json.dumps(response_json, indent=2)}")

        processor_response = ProcessorResponse(
            body=ResponseBody(
                amount=response_json.get("body").get("amount"),
                approved=response_json.get("body").get("approved"),
                failure_code=response_json.get("body").get("failure_code"),
                failure_message=response_json.get("body").get("failure_message"),
                approval_code=response_json.get("body").get("approval_code"),
                id=response_json.get("body").get("id"),
                card=ResponseBodyCard(
                    id=response_json.get("body").get("card").get("id"),
                    card_code=response_json.get("body").get("card").get("card_code"),
                    exp_year=response_json.get("body").get("card").get("exp_year"),
                    exp_month=response_json.get("body").get("card").get("exp_month"),
                    type=response_json.get("body").get("card").get("type"),
                    valid=response_json.get("body").get("card").get("valid"),
                ),
            )
        )
        return processor_response

    logger.error(f"Response from processor: {response.text}")
    raise Exception(f"Request to processor failed with status code {response.status_code}")
