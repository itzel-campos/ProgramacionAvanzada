#se debe haber importado json antes para poder utilizarla
import json 
# Serialización.
print(Estudiantes)
# Serialization
json_data = json.dumps(Estudiantes, default=lambda o: o.__dict__, indent=4)
print(json_data)
