# Category file for Sahayak
def find_category(problem):
      if ("scholarship" in problem or "exam" in problem or
        "study" in problem or "assignment" in problem or
        "attendance" in problem or "course" in problem or
        "result" in problem or "library" in problem):
        return "education"
      elif ("fever" in problem or "headache" in problem or
          "cold" in problem or "cough" in problem or
          "doctor" in problem or "hospital" in problem or
          "medicine" in problem or "health" in problem):
        return "health"
      elif ("ambulance" in problem or "accident" in problem or
          "danger" in problem or "fire" in problem or
          "police" in problem or "emergency" in problem):
        return "emergency"
      elif ("wifi" in problem or "internet" in problem or
          "network" in problem or "slow" in problem or
          "connection" in problem or "password" in problem):
        return "wifi"
      elif ("room" in problem or "warden" in problem or
          "mess" in problem or "water" in problem or
          "electricity" in problem or "cleaning" in problem or
          "hostel" in problem):
        return "hostel"
      elif ("python" in problem or "error" in problem or
          "code" in problem or "program" in problem or
          "loop" in problem or "function" in problem or
          "list" in problem or "dictionary" in problem):
        return "programming"
      elif ("faculty" in problem or "proctor" in problem or
          "vtop" in problem or "timetable" in problem or
          "notice" in problem or "registration" in problem):
        return "college"
      elif ("bus" in problem or "transport" in problem or
          "travel" in problem or "route" in problem):
        return "transport"
      elif ("fee" in problem or "payment" in problem or
          "refund" in problem or "financial" in problem):
        return "finance"
      elif ("hello" in problem or "hi" in problem or
          "help" in problem or "thanks" in problem or
          "thank" in problem or "bye" in problem):
        return "general"
      else:
        return "unknown"