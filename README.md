# service_Ticket_LLM2SAP
# 🤖 LLM + SAP RAP Integration Demo

A beginner-friendly demonstration project showing how **Large Language Models (LLMs)** can be integrated into enterprise applications using:

* 🧠 OpenRouter (LLM API access layer)
* 🐍 Python (backend orchestration)
* 🌐 Streamlit (UI layer)
* 🏢 SAP RAP (RESTful ABAP Programming Model)
* 🔗 OData V2 Web API (SAP communication layer)

This project is designed for **non-AI engineers, SAP developers, and beginners in LLM applications** who want to understand how modern AI systems connect with enterprise backend systems.

---

# 🎯 Purpose of this Demo

Modern enterprise systems are evolving from traditional transactional systems into **AI-assisted decision platforms**.

This demo shows:

* How a user can input raw text (incident / issue)
* How an LLM converts it into structured business data
* How SAP RAP persists that data in a backend system
* How OData acts as the bridge between frontend and backend

---

# 🧠 High-Level Concept (Simple Explanation)

Think of this system like a pipeline:

```
User Input → LLM Processing → Structured JSON → SAP OData → RAP Backend → Database
```

### In simple terms:

> A user writes something in English → AI understands it → converts it into structured SAP data → SAP stores it

---

# 🏗️ System Architecture

```
                ┌────────────────────┐
                │   Streamlit UI     │
                │ (Frontend Layer)   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Python Backend     │
                │ (Orchestration)    │
                └─────────┬──────────┘
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
 ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
 │ OpenRouter   │  │ JSON Mapper  │  │ SAP OData V2 │
 │ (LLM API)    │  │ Formatter    │  │ Web Service  │
 └──────────────┘  └──────────────┘  └──────┬───────┘
                                            │
                                            ▼
                                ┌────────────────────┐
                                │ SAP RAP Backend    │
                                │ (ABAP Layer)       │
                                └─────────┬──────────┘
                                          ▼
                                ┌────────────────────┐
                                │ Database Table     │
                                │ (ZAI_INCIDENT)     │
                                └────────────────────┘
```

---

# 🧩 Components Explained

## 1. 🖥️ Streamlit (UI Layer)

Streamlit is used to create a simple web interface where users can:

* Enter raw text (incident description)
* Click submit
* View AI-generated structured output

### Why Streamlit?

* Very fast to build UI
* No frontend framework needed
* Ideal for prototypes and demos

---

## 2. 🐍 Python Backend

Python acts as the **brain orchestrator**:

It handles:

* Sending user input to LLM
* Receiving structured JSON response
* Cleaning / validating JSON
* Sending data to SAP via OData

---

## 3. 🧠 OpenRouter (LLM Layer)

OpenRouter is used to access LLM models via API.

### What it does here:

* Takes raw user text
* Converts it into structured JSON

### Example:

#### Input:

```
User: "SM30 table not allowing new entries"
```

#### LLM Output:

```json
{
  "raw_input": "SM30 table not allowing new entries",
  "business_summary": "User cannot add entries via SM30",
  "technical_summary": "Table maintenance view issue or missing authorization",
  "priority": "Medium",
  "sap_module": "ABAP"
}
```

---

## 4. 🔄 JSON Processing Layer

Before sending data to SAP:

* JSON is validated
* Missing fields are handled
* Default values are inserted if required

This ensures SAP always receives clean structured data.

---

## 5. 🔗 SAP OData V2 Web API

This is the communication bridge between Python and SAP.

### Responsibilities:

* Accept POST requests from Python
* Trigger RAP behavior implementation
* Persist data into ABAP table
* Return response (201 Created)

---

## 6. 🏢 SAP RAP (Backend Layer)

RAP handles:

* Business logic
* Data validation
* UUID generation
* Default field population
* Persistence to database

### Key responsibilities:

* Auto-generate `incident_id`
* Set `created_at`
* Set `created_by`
* Enforce status rules

---

## 7. 🗄️ Database Layer

Table: `ZAI_INCIDENT`

Stores final structured output:

* Incident details
* AI-generated summaries
* Metadata

---

# 🔄 End-to-End Flow

## Step-by-step execution:

1. User enters text in Streamlit UI
2. Python sends request to OpenRouter
3. LLM returns structured JSON
4. Python formats and validates JSON
5. Python sends POST request to SAP OData API
6. SAP RAP processes request
7. RAP fills missing fields (UUID, timestamps)
8. Data is saved in database
9. SAP returns HTTP 201 Created
10. Streamlit displays success response

---

# 📦 Example Request Flow

## Input (User)

```
SM30 is not allowing me to create entries in ZBILL table
```

## LLM Output

```json
{
  "raw_input": "SM30 issue",
  "business_summary": "User cannot create entries in ZBILL via SM30",
  "technical_summary": "Missing table maintenance configuration",
  "priority": "High",
  "sap_module": "ABAP"
}
```

## SAP Response

```json
{
  "d": {
    "incident_id": "generated-uuid",
    "status": "PROCESSED",
    "created_at": "timestamp",
    "created_by": "SAPUSER"
  }
}
```

---

# ⚙️ Key Technologies Used

| Layer         | Technology         |
| ------------- | ------------------ |
| UI            | Streamlit          |
| Backend       | Python             |
| LLM API       | OpenRouter         |
| SAP Interface | OData V2           |
| SAP Backend   | RAP (ABAP)         |
| Database      | SAP HANA / Z Table |

---

# 🚨 Common Issues in This Architecture

## 1. Missing UUID

* Usually caused by incorrect RAP numbering configuration

## 2. 200 instead of 201

* Happens when update is triggered instead of create

## 3. Empty fields in response

* Determination not executed correctly

## 4. Authentication errors

* SAP BTP session expiry or incorrect service binding

---

# 💡 Why This Architecture is Powerful

This system demonstrates:

* AI transforming unstructured text → structured business data
* Seamless integration between modern AI APIs and SAP systems
* Enterprise-grade backend processing with RAP

---

# 🧠 Learning Outcome

After understanding this demo, you will know:

* How LLMs are used in real enterprise systems
* How SAP RAP handles business logic
* How APIs connect AI systems with ERP
* How modern full-stack AI applications are built

---

# 📌 Summary

This project is a **bridge between AI and enterprise SAP systems**, showing how:

> Natural language → AI → structured data → SAP persistence

---


## Snapshots of the application 

Start the application by rough input 

<img width="1821" height="494" alt="image" src="https://github.com/user-attachments/assets/3f0e039c-6893-438a-bc9d-e582036d61b5" />

-----------------------------------
LLM categorizes based on prompt 

<img width="1816" height="807" alt="image" src="https://github.com/user-attachments/assets/d3043fde-bb6e-4bf5-8f7c-c97d91bc5cc7" />

------------------------------------
Further output 
<img width="1835" height="807" alt="image" src="https://github.com/user-attachments/assets/659ede7b-2b1b-4e36-9677-58e39b27a34c" />

-------------------------------------
<img width="1588" height="842" alt="image" src="https://github.com/user-attachments/assets/0a90cb30-3375-48a9-a3ca-df7d593eac05" />

---------------------------------------
You can see it appended in your table in ADT - Eclipse
<img width="1892" height="532" alt="image" src="https://github.com/user-attachments/assets/a8f638cd-1de1-446c-ad18-d70323d84a83" />

-----------------------------------------
Video 

https://github.com/user-attachments/assets/eba85d3c-5221-4138-af02-27a7685219d3





