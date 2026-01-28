import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="add",
    description="Add two numbers",
    toolProperties=json.dumps([
        {"propertyName": "a", "propertyType": "integer", "description": "First number"},
        {"propertyName": "b", "propertyType": "integer", "description": "Second number"}
    ])
)
def add(context) -> str:
    """Add two numbers"""
    content = json.loads(context)
    a = content["arguments"]["a"]
    b = content["arguments"]["b"]
    result = a + b
    return str(result)


@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="count_letters_in_word",
    description="Count occurrences of a letter in a word",
    toolProperties=json.dumps([
        {"propertyName": "word", "propertyType": "string", "description": "The word to search in"},
        {"propertyName": "letter", "propertyType": "string", "description": "The letter to count"}
    ])
)
def count_letters_in_word(context) -> str:
    """Count occurrences of a letter in a word"""
    content = json.loads(context)
    word = content["arguments"]["word"]
    letter = content["arguments"]["letter"]
    result = word.lower().count(letter.lower())
    return str(result)
