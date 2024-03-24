import os
import warnings
from typing import Dict
from chatbot_utils import get_answer
from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass


############################################################
# Callback function called on update config 
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    for text in request.text:
        response = get_answer(text)
        output.append(response)
    return SchemaUtil.create(SimpleText(), dict(text=output))
