# Task 1: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

### College Student Attendance & Exam Eligibility

This project compares three approaches for answering questions about a student's
attendance and examination eligibility.

The private student data used in this scenario is:

- Student: Arun
- Course: AI & DS
- Attendance: 82%
- Internal Mark: 76

For this scenario, we assume that a student is eligible for the end-semester
examination when:

- Attendance is at least 75%
- Internal mark is at least 40%

Therefore, Arun is eligible for the examination.

---

## 2. Plain Chatbot

The plain chatbot sends the user's question directly to an LLM.

It does not have access to Arun's private student data and does not use any
external tools.

### How it works

```text
User Question
      ↓
     LLM
      ↓
   Answer