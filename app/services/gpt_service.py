from models.gpt_message import GptMessage

from App import client_gpt, app

def get_resume_text():
    
    resume_text = ""
    
    with open("../resource/recognized.txt", "r", encoding="utf-8") as file:
        for line in file:
            resume_text += line
    
    return resume_text


def get_gpt_assessment(resume_text: str, job_requirement: str) -> GptMessage:
    """
    return dict
    {
        "Applicant": str,
        "Email": str,
        "Phone": str,
        "Link": dict[str, str],
        "Position": str,
        "Major": str,
        "Skill Match Score": int,
        "Experience Score": int, 
        "Interview Questions": list[str]
    }
    """
    response = client_gpt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                Disregarding previous information. You are the human resources manager, and you are given the resume (text) and job requirements (JSON). 
                You need to view the resume, and output the infomation in following json format: 
                {"Applicant":"(Applicant's Name)", "Email":"(Applicant's email)", "Phone":"(phone number)", "Link":{"(link1)":"(url1)", "(link2)":"(url2)"}, "Position": "(mostly described job position)", "Major": "(Highest degree major) ", "Skill Match Score": (1-10), "Experience Score": (1 -10), "Interview Questions": [(Question 1), (Question 2), ...]}. 
                First, for "Applicant", "Email", "Phone", "Link", "Position", "Major", extract the applicant's name, email, phone number and related websites (possibly multiple) from the resume, and if there is any lack of value of any key, store "None" in the value. 
                Second, for "Match skill Score", "Experience Score", check whether the applicant meets the given job requirements based on the resume. For "Skill Match Score" and "Experience Score", check whether the applicant meets the skills, experience requirements, you scores these aspect of the applicant (1-10).
                Last, for "Interview Questions", generate some questions that can be asked during the interview based on the information in the resume.
            """}, 

            {"role": "user", "content": f"""
                Job Requirement:
                {job_requirement}
                Resume text:
                {resume_text}
            """}
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.choices[0].message.content

    return GptMessage(response_text)
