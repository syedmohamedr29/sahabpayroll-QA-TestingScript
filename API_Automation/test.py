import requests

def test_get_demographic_breakup():
    authToken = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1MTE2QTFFNDg0MkY1MzlGREQzOUE1NDcxQjM4NUQxOTRFM0E5OTciLCJ4NXQiOiJoUkZxSGtoQzlUbjkwNXBVY2JPRjBaVGpxWmMiLCJ0eXAiOiJhdCtqd3QifQ.eyJzdWIiOiIzYTE5MWM5MC02MDc0LWEzOTEtMDk4Mi05YWY0OGZlYTRlNmQiLCJ0ZW5hbnRpZCI6IjNhMTkxYzkwLTVkZGQtYjA2Ni04NzVkLWRmYmExNDhkYWY5MSIsInVuaXF1ZV9uYW1lIjoiVGVuYW50QWRtaW4iLCJDb21wYW55SWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJFbXBsb3llZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiRW1wbG95ZWVDb2RlIjoiIiwiQWNjZXNzaWJsZUNvbXBhbnlJZHMiOiIiLCJvaV9wcnN0IjoiV2ViIiwib2lfYXVfaWQiOiIzYTE5MWM5Ni04MzRmLWNhODEtYjE1My1iMzBhMWUwOTUwMzUiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJUZW5hbnRBZG1pbiIsInJvbGUiOiJUZW5hbnRBZG1pbiIsImVtYWlsIjoic3llZC5tb2hhbWVkQGNvbW0taXQuaW4iLCJlbWFpbF92ZXJpZmllZCI6IlRydWUiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiOiJGYWxzZSIsImNsaWVudF9pZCI6IldlYiIsIm9pX3Rrbl9pZCI6IjNhMWFjZGYyLTc3MDgtZWMyYy05NmZkLTJkMWE0MTM4MTU4ZiIsImF1ZCI6WyJJZGVudGl0eVNlcnZpY2UiLCJTYWFzU2VydmljZSIsIkFkbWluaXN0cmF0aW9uU2VydmljZSIsIkxlYXZlU3ZjIiwiRW1wbG95ZWVTdmMiLCJDb21wYW55U3ZjIiwiQWNjb3VudFNlcnZpY2UiLCJDb21wQmVuZWZpdHNTdmMiXSwic2NvcGUiOiJvZmZsaW5lX2FjY2VzcyBvcGVuaWQgcHJvZmlsZSBlbWFpbCBwaG9uZSBBY2NvdW50U2VydmljZSBJZGVudGl0eVNlcnZpY2UgQWRtaW5pc3RyYXRpb25TZXJ2aWNlIENvbXBhbnlTdmMgU2Fhc1NlcnZpY2UgRW1wbG95ZWVTdmMgQ29tcEJlbmVmaXRzU3ZjIExlYXZlU3ZjIiwianRpIjoiYjRmYmEyZGQtYjUzMS00ZWExLTkxZDQtMmRiZjcyOGNmMWVlIiwiaXNzIjoiaHR0cHM6Ly9hdXRoOC5kZXYuem9vbHdvcmsuY29tLyIsImV4cCI6MTc1MTIxOTk4MCwiaWF0IjoxNzUxMjAxOTgwfQ.vDKdzS2mLj_EmlyH178HvxOGmcR5bWjBE6As7DvVoMlUcwJBU19xQ28FRfPy8OuERq7uRS8mD9MH3J0tabwkWIpD1oJmTD-LiLo1Wgiji0U1ARheHY4Q9LWvxJf8PNfzZMEdHxSQhJdEZYRe9PKMoPOR1qWx8ogWgUAWZ8-rzw0Ad-8bnNzZDb0xTFZh9laLRKwLYDVcxQR-YYPhwL_g9luJ-RWgT1qznraZoFROUCfSzT-H_RiWIOY_FGD6ZSQth6As3T61avj36BGI5NwaokRk-YL9pbfYGOyvpCNJGqmjBFNu14ROOMNs6JG4WlnTwMuzGmDQydKkNhu4eVVpXQ"  # (trimmed for readability)

    baseURL = "https://employee8.dev.zoolwork.com/api/Employees/dashboard/demographicBreakup"

    headersGET = {
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'Authorization': authToken
    }

    params = {
        "companyId": "3a191c9d-64cd-7600-c591-e2c5663f9b75",
        "country": "152",
        "startDate": "2024-07-01T00:00:00.000Z",
        "endDate": "2025-06-30T00:00:00.000Z"
    }

    response = requests.get(url=baseURL, headers=headersGET, params=params)
    print("Status Code:", response.status_code)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Response JSON Data:", response.json())

    data = response.json()

    #for item in data:
    #    print(f"Month: {item['date']}, Total Employees: {item['totalNoOfEmployees']}")

    total_employees = [item['totalNoOfEmployees'] for item in data]
    print(total_employees)