import json


def role_requirements(role):
    with open("roles.json", "r") as file:
        roles = json.load(file)

    role = role.lower().strip()

    role_data = roles.get(role)

    if role_data is None:
        return {
            "error": f"Role '{role}' was not found.",
            "available_roles": list(roles.keys())
        }

    return role_data["skills"]


def get_roadmap(role, missing_skills):
    with open("roles.json", "r") as file:
        roles = json.load(file)

    role = role.lower().strip()

    role_data = roles.get(role)

    if role_data is None:
        return {}

    roadmap = role_data.get("roadmap", {})

    result = {}

    for skill in missing_skills:
        if skill in roadmap:
            result[skill] = roadmap[skill]

    return result


def skill_gap(user_skills, required_skills):
    missing = []

    for skill in required_skills:
        if skill not in user_skills:
            missing.append(skill)

    return missing


def weekly_plan(roadmap):
    plan = []

    for skill, topics in roadmap.items():
        for topic in topics:
            plan.append({
                "skill": skill,
                "topic": topic
            })

    return plan[:7]


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "role_requirements",
            "description": "Find the skills required for a specific job role.",
            "parameters": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "description": "The job role the user wants to target."
                    }
                },
                "required": ["role"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_roadmap",
            "description": "Find the learning roadmap for the skills the user is missing.",
            "parameters": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "description": "The job role the user wants to target."
                    },
                    "missing_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Skills the user is missing."
                    }
                },
                "required": ["role", "missing_skills"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "skill_gap",
            "description": "Compare the user's skills with the required skills and find missing skills.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Skills the user already has."
                    },
                    "required_skills": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "Skills required for the role."
                    }
                },
                "required": ["user_skills", "required_skills"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "weekly_plan",
            "description": "Create a 7-day learning plan from the user's roadmap.",
            "parameters": {
                "type": "object",
                "properties": {
                    "roadmap": {
                        "type": "object",
                        "description": "The learning roadmap returned by get_roadmap."
                    }
                },
                "required": ["roadmap"]
            }
        }
    }
]


TOOL_FUNCTIONS = {
    "role_requirements": role_requirements,
    "skill_gap": skill_gap,
    "get_roadmap": get_roadmap,
    "weekly_plan": weekly_plan
}