###########
# Mock objects to mimick responses from OpenAI server
###########

import json

class DotDict:
    """A dictionary-like object that supports dot notation and displays as a dictionary in Jupyter."""
    
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DotDict(value))
            elif isinstance(value, list):
                setattr(self, key, [DotDict(i) if isinstance(i, dict) else i for i in value])
            else:
                setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def to_dict(self):
        """Convert back to a dictionary"""
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def __repr__(self):
        """Make it display like a dictionary in Jupyter Notebook"""
        return json.dumps(self.to_dict(), indent=2)

# Mock OpenAI ChatCompletion response
mock_response_exercise = DotDict( 
        {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1700000000,
        "model": "gpt-4o",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Die Aufgabe ist fast richtig gelöst."
                },
                "logprobs": None,
                "finish_reason": "stop"
            },
            {
                "index": 1,
                "message": {
                    "role": "assistant",
                    "content": "Die Aufgabe ist richtig gelöst :D"
                },
                "logprobs": None,
                "finish_reason": "stop"
            }
        ],
        "usage": None,
        "system_fingerprint": None
    }
)


mock_response = DotDict(
        {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1700000000,
        "model": "gpt-4o",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Hi there, this is the mock response, not a real LLM response."
                },
                "logprobs": None,
                "finish_reason": "stop"
            },
        ],
        "usage": None,
        "system_fingerprint": None
    }
)


mock_json_response = DotDict({
        "id": "cmpl-12345",
        "object": "text_completion",
        "created": 1700000000,
        "model": "gpt-4",
        "choices": [
            {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": """{\n  \"mountain\": \"Matterhorn\",\n  \"relations\": [\n    {\n      \"person_name\": \"Schmid brothers\",\n      \"is_mountaineer\": true,\n      \"climbed_mountain\": true\n    },\n    {\n      \"person_name\": \"Günther Oskar Dyhrenfurth\",\n      \"is_mountaineer\": true,\n      \"climbed_mountain\": null\n    }\n  ]\n}"""
            },
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 200,
            "completion_tokens": 50,
            "total_tokens": 250
        }
    })






