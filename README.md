# Birthday API APP

This projects contains the files for the deployment of a API based on FastAPI and relies on PostegreSQL. The deployment is based on helm chart and minikube.

## The requirement

1. Code a simple application that exposes the following HTTP based APIs:

    **Description**: Save/updates a given user name and date of birth in a database.  
    **Request**: PUT `/hello/<username>` `{ “dateOfBrith”: “YYYY-MM-DD” }`  
    **Response**: 204 No Content

    **Note**:
    - Username should only be letters.  
    - YYYY-MM-DD must be a date before today's date.

    **Description**: Returns a birthday message  
    **Request**: GET `/hello/<username>`  
    **Response**: 200 ok  
    **Response examples**:  
    1. If username's birthday is in N days  
    `{ “message”: “Hello, <username>! Your birthday is in N day(s)”}`
    2. If username's birthday is today  
    `{ “message”: “Hello, <username>! Happy birthday!” }`

    **Note**:
    - Use the storage or DB of your choice.

2. Code a simple helm chart and deploy this application into a small local kubernetes cluster
(like minikube or k3s)

3. Produce a system diagram of how this solution would be deployed into AWS. You
can consider that the application is of high criticality and high usage, so add all the components you deem required to achieve a strong and resilient nfrastructure.

## Main features

### API

- Main stack is based on Python
- Uses Pydantic and SQL model for types definitions
- Implements the following API methods
  - **PUT** for register a new record based on a name and birthday date.
  - **GET** to retrieve days for the next birthday and for /health status.
- Data validation:
- Using different Pydantic libraries, to ensure data consistency.

### Database

- Uses PostgreSQL to store the data
- Implements Networks policies for Zero Trust approach.

### Helm Charts

The design of the charts and the architectures considers:

- **Autoscaling:** Configuration of the HPA based on CPU use.
- **Security:** NetworkPolicies at namespace level for database namespace.
- **Governance:** Uses ResourceQuotas to control the use of resources and limits for the deployments. 
- **Data persistency:** Using Persistent volumes and Persistent Volume Claims to guarantee data persistency at database level.
