import json

class GptMessage:
    def __init__(self, original_text):
        self.original_text = original_text

    def parse_json(self) -> dict:

        try:
            data_dict = json.loads(self.original_text)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)

        return data_dict


# Example usage:
message = GptMessage("""
            {"Position": "Manufacturing Engineer", "Same position": "Yes", "Skill matching score": 8, "Experience score": 7, "Interview questions": ["Can you provide examples of process improvements you have implemented in your previous roles?", "Tell me about your experience with lean principles and continuous improvement.", "Have you worked on any projects involving Design for Manufacturability?", "How proficient are you in using AutoCAD?"]}
        """)
# job_content = message.parse_job_content()
assessment = message.parse_json()

# print(job_content)
for key, value in assessment.items():
    print(f"Key: {key}, Value: {value}")
