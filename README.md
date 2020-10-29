# About the project:
This is my final project for Udacity full stack nano-degree course, it's a deployed API with Authentication for managing casting agency, you can add movies, actors and manage them based on the role you have.

# Backend Docs (Endpoints docs and testing):
[View the README.md within ./backend for more details.](./backend/README.md)


# Login information
## Login link:
```
Direct login link:
https://udacitycastingagency.eu.auth0.com/authorize?audience=castingAgency&response_type=token&client_id=3ABxPK2MGT0K6vxWuHTqQnaCWBKYMMcX&redirect_uri=http://localhost:5000/
```
```
API link: https://udacity-casting-agency-api.herokuapp.com/
```
## User 1:
```
Type:
Casting Assistant
Email:
castingAssis@castingagency.com
Password:
iamCastingAssis@
Token: (26/Oct/2020)
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRqNWJnQkVaYTY4c0Ewc09tSTZlRSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHljYXN0aW5nYWdlbmN5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1Zjk2YzExZmM1ZmI2MzAwNzk2NGIxOGUiLCJhdWQiOiJjYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjAzOTY2MDMyLCJleHAiOjE2MDQwNTI0MzIsImF6cCI6IjNBQnhQSzJNR1QwSzZ2eFd1SFRxUW5hQ1dCS1lNTWNYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.DvHpGwcae9PRTtJX9qiK_qVWEHyzV7EkA-uQx7rxNC5nKtgBapJHeK4PBL3yULFDrxAAMj5hhO3HujB_u5j9m3q7C3esZf1MbMZGObX9fqI6Tm4ais23wef_9dC8S9nM8aQyU1Qy99YMhf1GgCQy6Z3_LN5tXl1ablhizKNJzKDGpvyoJnRjCNAO0C60UJ-102aV7jE0qWAkhqjHoPzAAjuhZ7xMHpK1vppqVguYJmG0pXZEXN3vOf9KW7N1NUVuiuimHCne8IymZKXiUKNmIQgEj_IFQdDv8HJtRI55nirC-ZHN0PMbN16P8HrN5Pn-p7BQ2Rx3W9G894KfVi9Oiw
```
## User 2:
```
Type:
Casting Director
Email:
castingDirector@castingagency.com
Password:
iamCastingDirector@
Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRqNWJnQkVaYTY4c0Ewc09tSTZlRSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHljYXN0aW5nYWdlbmN5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1Zjk2YzFjNmM1ZmI2MzAwNzk2NGI1M2YiLCJhdWQiOiJjYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjAzOTY2MDg1LCJleHAiOjE2MDQwNTI0ODUsImF6cCI6IjNBQnhQSzJNR1QwSzZ2eFd1SFRxUW5hQ1dCS1lNTWNYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.CGEhzQs5YYcpb0uZ8s1lP1LWeih8UCCp0c5n8qZJoSYXq9_h3kZM3ubgSy0XoptraAhTicAMstbjBLapV-MBYP88X0O3mP88X31G0tjQ27Ddbll7TzWd78OvbVdWYzVUkBoUnjHgvvglvZj2eN6xX0rsaXq004vtYhZ2RjBS8DuBVUoRVW98G5aJhiG7mTACcB8kCK4fRTgygqWhNsiRxLrsfGJEx-iFzo2TtiMDenThxlvX8yNuB4QXzp2mAeVc5AccHh4JxcWE2vVUPm--o_NQLkfPM9p5-37RriXPOyuHLhraptaJzsEltSXiIfnetRq3uFRfc2oExCpW4GILvQ
```
## User 3:
```
Type:
Casting Producer
Email:
castingProducer@castingagency.com
Password:
iamCastingProducer@
Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRqNWJnQkVaYTY4c0Ewc09tSTZlRSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHljYXN0aW5nYWdlbmN5LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1Zjk2YzFkN2ZhMDk1ZjAwNzUyMzY3MTIiLCJhdWQiOiJjYXN0aW5nQWdlbmN5IiwiaWF0IjoxNjAzOTY2MTE3LCJleHAiOjE2MDQwNTI1MTcsImF6cCI6IjNBQnhQSzJNR1QwSzZ2eFd1SFRxUW5hQ1dCS1lNTWNYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.qljS08tcUuSwwBP_Q5KM9SsdKXhCkbPlJhUhcgcaCbbiOF9uyA-HirQw3vQH6xrOwmzSqHl1Z1mojedolmhcOMk27Yna6GxsexBAMZO4LM4d_MMoRbh2RL3MWV_PipZWScBt1aZCTcWw3FbB9g_FSKrDq5VLMg5iTO3PY43ynDwf8FX2awqfdGKmtKkIzDA3LFxU3kzUSC1A3BOeZtmQCZtms0JPqh9sV8YkGo-zNU5CTtg6-HPmm5fF0Fe-iwvLBlj_Qy4u_D-XEt0ULDPC2BCX_t4TdAV1RgYp6NYpcEL3s6ob6tRFEGbFY1AzZPElSKA_92_TMbgAu2Nb2dUYzQ
```

