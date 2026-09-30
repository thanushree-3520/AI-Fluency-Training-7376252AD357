COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        fee = COURSE_FEES[course_code]
        return f"{course_code} course fee is ₹{fee}"
    else:
        return f"{course_code} course not found"


def tool_call(course_code):
    return get_course_fee(course_code)


if __name__ == "__main__":
    print("College Course Fee Lookup Tool")
    print("--------------------------------")

    print(tool_call("CS101"))
    print(tool_call("AI202"))
    print(tool_call("DS303"))
    print(tool_call("XYZ101"))