# SkillBridge: Edge Proctoring Proof of Concept (PoC)

## 📌 What is this?
This is a lightweight technical Proof of Concept built for **Smart India Hackathon 2026**. It validates the architectural feasibility of the SkillBridge assessment security layer (Slide 4 of our presentation).

## ⚙️ Why it matters (The Feasibility Proof)
Traditional proctoring software streams heavy webcam video to a central server for AI analysis, requiring massive bandwidth and incurring high cloud computing costs. 

SkillBridge operates differently. As demonstrated in this PoC, we utilize **Client-Side Edge Computing**:
1. **Zero-Bandwidth Tab Locking:** Utilizes the native Page Visibility API to instantly detect OS-level window minimizing or tab switching.
2. **Edge Audio VAD (Voice Activity Detection):** Utilizes the Web Audio API to process microphone frequency arrays locally on the student's browser. If unauthorized talking is detected, only a tiny text payload (the violation log) is sent via WebSockets, completely eliminating the need for streaming audio to a server.

## 🚀 Try it Live
https://gojiyabrijesh.github.io/skillbridge-proctoring-poc/
