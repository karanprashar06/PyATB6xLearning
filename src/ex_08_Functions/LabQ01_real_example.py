def validate_status_code(response_code):
     if response_code > 0:
         if response_code == 200:
             print("The response code is valid")
         else:
             print("The response code is invalid")
     else:
         print("The response code is invalid")

validate_status_code(200)
validate_status_code(404)
validate_status_code(1222)
validate_status_code(response_code=200)
