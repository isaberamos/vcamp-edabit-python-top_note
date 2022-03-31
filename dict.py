def top_note(student):
    return {"name": student["name"], "top_note": max(student["notes"])}   # Retornará o nome do aluno e a nota máxima

